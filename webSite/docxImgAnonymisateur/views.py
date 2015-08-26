# coding: utf-8
import shutil
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from .forms import *
from .includes.anonymiser_images_docx import process
from django.core.servers.basehttp import FileWrapper

# entier utilisé pour ne pas avoir 2 dossiers du même nom
manual_lock = 0


#
def clean(absolute_path):
    global manual_lock
    # on attend que tout le monde ait fini d'ecrire dans les dossiers
    while manual_lock != 0:
        pass
    for the_file in os.listdir(absolute_path):
        file_path = os.path.join(absolute_path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception, e:
            print e


# récupère les demandes de find/replace de l'utilisateur
# sous la forme de {'mot à rechercher': 'mot à substituer'}
def get_hash_f_r(posts):
    res = {}
    if posts['texte_final']:
        res[posts['texte_original']] = posts['texte_final']
    for i in range(0, int(posts['extra_field_count'])):
        value = posts['extra_texte_final_{index}'.format(index=i)]
        clef = posts['extra_texte_original_{index}'.format(index=i)]
        if value and clef:
            res[clef] = value
    return res


@csrf_protect
@never_cache
@sensitive_post_parameters()
@login_required
def index(request):
    # entier utilisé pour ne pas avoir 2 dossiers du même nom
    global manual_lock
    # le chemin vers le dossier où le fichier à anonymiser sont téléchargés
    dirty_path = os.path.join(os.path.join(os.path.dirname(__file__), 'includes'), 'doc_a_anonymiser')
    # le chemin vers le dossier où le fichier anonymisé va être construit
    cleaned_path = os.path.join(os.path.join(os.path.dirname(__file__), 'includes'), 'doc_anonyme')
    # suppression des fichiers 'temporaires'
    clean(dirty_path)
    clean(cleaned_path)
    if request.method == 'POST':
        form = DocxUploadFileForm(request.POST, request.FILES, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            manual_lock += 1
            # on construit un chemin de fichier unique correspondant au fichier que l'utilisateur nous envoie pour anonymisation
            dirty_path_file = os.path.join(dirty_path, str(manual_lock) + '.docx')
            # idem on construit un chemin de fichier unique correspondant au fichier anonyme que l'on va construire
            filename = os.path.join(cleaned_path, 'anonyme_' + str(manual_lock) + '.docx')
            # le nom tel que le verra l'utilisateur lorsqu'il récupèrera le fichier anonyme
            download_name = 'anonymise.docx'
            # sous la forme {'mot à rechercher': 'mot à substituer'}
            hash_find_replace = get_hash_f_r(request.POST)
            try:
                with open(dirty_path_file, 'wb') as destination:
                    for chunk in request.FILES['fichier'].chunks():
                        destination.write(chunk)
                # voir includes/anonymiser_images_docx.py
                process(dirty_path_file, cleaned_path, form.cleaned_data['niveau_de_flou'], hash_find_replace)

                wrapper = FileWrapper(open(filename))
                response = HttpResponse(wrapper, content_type='docx')
                response['Content-Length'] = os.path.getsize(filename)
                response['Content-Disposition'] = "attachment; filename=%s" % download_name

                manual_lock -= 1
                return response
            except Exception as e:
                print e
                manual_lock -= 1
                return render(request, 'docxImgAnonymisateur/index.html', locals())
    else:
        form = DocxUploadFileForm()
    return render(request, 'docxImgAnonymisateur/index.html', locals())

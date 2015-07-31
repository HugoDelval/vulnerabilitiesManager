# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .forms import SearchVulnForm, SearchRecoForm
from .models import Vulnerabilite, Recommandation, ActiviteAudit


class VulnDetailView(generic.DetailView):
    model = Vulnerabilite
    # template_name = 'vuln/vulnerabilite_detail.html'

    @csrf_protect
    @never_cache
    @login_required
    def dispatch(self, *args, **kwargs):
        return super(VulnDetailView, self).dispatch(*args, **kwargs)


class RecoDetailView(generic.DetailView):
    model = Recommandation
    # template_name = 'vuln/recommandation_detail.html'

    @csrf_protect
    @never_cache
    @login_required
    def dispatch(self, *args, **kwargs):
        return super(RecoDetailView, self).dispatch(*args, **kwargs)


@csrf_protect
@never_cache
@login_required
def displayVuln(request):
    vulnerabilite_list = Vulnerabilite.objects.all()
    form = SearchVulnForm()
    return render(request, 'vuln/vulnerabilite_list.html', locals())


def cast(chaine):
    try:
        ret = int(chaine)
        return ret
    except ValueError:
        return -1


@sensitive_post_parameters()
@csrf_protect
@never_cache
@login_required
def searchVuln(request):
    if request.method == "POST":
        activite_parente = None
        index_modifie = cast(request.POST.get('index_modifie', -1))
        id_activite = cast(request.POST.get('activites_liees_{i}'.format(i=index_modifie), 0))
        try:
            activite_parente = ActiviteAudit.objects.get(pk=id_activite)
        except ActiviteAudit.DoesNotExist:
            activite_parente = None
        print activite_parente
        form = SearchVulnForm(request.POST, activite_parente=activite_parente)
        if form.is_valid():
            vulnerabilite_list = []
            mot_clef = form.cleaned_data["mot_clef"]
            desc = form.cleaned_data["recherche_dans_la_description_de_la_vuln"]
            vulnerabilite_list1 = Vulnerabilite.objects.filter(mots_clefs__nom__icontains=mot_clef, description__icontains=desc)
            for vuln in vulnerabilite_list1:
                for activite in vuln.activites_liees.all():
                    if activite.isEnfant(activite_parente):
                        vulnerabilite_list.append(vuln)
                        break
        else:
            error_message = 'Votre requête contient des erreurs, veuillez réessayer svp.'
        return render(request, 'vuln/vulnerabilite_list_body.html', locals())
    else:
        return redirect(reverse('vuln:index'))


@csrf_protect
@never_cache
@login_required
def displayReco(request):
    recommandation_list = Recommandation.objects.all()
    form = SearchRecoForm()
    return render(request, 'vuln/recommandation_list.html', locals())


@sensitive_post_parameters()
@csrf_protect
@never_cache
@login_required
def searchReco(request):
    if request.method == "POST":
        form = SearchRecoForm(request.POST)
        if form.is_valid():
            expl = form.cleaned_data["recherche_dans_explication_reco"]
            recommandation_list = Recommandation.objects.filter(explication__icontains=expl)
        else:
            error_message = 'Votre requête contient des erreurs, veuillez réessayer svp.'
        return render(request, 'vuln/recommandation_list.html', locals())
    else:
        return redirect(reverse('vuln:recos'))
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
import operator

from .forms import SearchVulnForm, SearchRecoForm
from .models import Vulnerabilite, Recommandation, ActiviteAudit, MotClef


class VulnDetailView(generic.DetailView):
    model = Vulnerabilite
    # template_name = 'vuln/vulnerabilite_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VulnDetailView, self).dispatch(*args, **kwargs)


class RecoDetailView(generic.DetailView):
    model = Recommandation
    # template_name = 'vuln/recommandation_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecoDetailView, self).dispatch(*args, **kwargs)


@login_required
def displayVuln(request):
    vulnerabilite_list = Vulnerabilite.objects.all()
    vuln_mots_clefs = MotClef.objects.all()
    form = SearchVulnForm()
    return render(request, 'vuln/vulnerabilite_list.html', locals())


def cast(chaine):
    try:
        ret = int(chaine)
        return ret
    except ValueError:
        return -1


def getQueryForMotsClefsAndDescription(cleaned_data):
    s = cleaned_data["mots_clefs"]
    mots_clefs = s.split('-')
    if len(mots_clefs) > 1:
        mots_clefs.pop()
    mots_clefs_selectionnes = MotClef.objects.filter(reduce(operator.or_, (Q(nom=item) for item in mots_clefs)))
    desc = cleaned_data["recherche_dans_la_description_de_la_vuln"]
    if mots_clefs_selectionnes:
        return reduce(operator.and_, (Q(mots_clefs=item, description__icontains=desc) for item in mots_clefs_selectionnes)), mots_clefs_selectionnes
    else:
        return Q(description__icontains=desc), []


@sensitive_post_parameters()
@csrf_protect
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
        form = SearchVulnForm(request.POST, activite_parente=activite_parente)
        if form.is_valid():
            vulnerabilite_list = []
            query, mots_clefs_selectionnes = getQueryForMotsClefsAndDescription(form.cleaned_data)
            vulnerabilite_list1 = Vulnerabilite.objects.filter(query)
            for vuln in vulnerabilite_list1:
                for activite in vuln.activites_liees.all():
                    if activite.isEnfant(activite_parente):
                        vulnerabilite_list.append(vuln)
                        break
            vuln_mots_clefs = MotClef.objects.all()
        else:
            error_message = 'Votre requête contient des erreurs, veuillez réessayer svp.'
        return render(request, 'vuln/vulnerabilite_list_body.html', locals())
    else:
        return redirect(reverse('vuln:index'))


@login_required
def displayReco(request):
    recommandation_list = Recommandation.objects.all()
    form = SearchRecoForm()
    return render(request, 'vuln/recommandation_list.html', locals())


@sensitive_post_parameters()
@csrf_protect
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
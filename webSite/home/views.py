# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import  HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Q

from .forms import SearchVulnForm, SearchRecoForm
from .models import Vulnerabilite, Recommandation


class VulnDetailView(generic.DetailView):
    model = Vulnerabilite
    # template_name = 'home/vulnerabilite_detail.html'


class RecoDetailView(generic.DetailView):
    model = Recommandation
    # template_name = 'home/recommandation_detail.html'


def displayVuln(request):
    vulnerabilite_list = Vulnerabilite.objects.all()
    form = SearchVulnForm()
    form.updateActivites()
    return render(request, 'home/vulnerabilite_list.html', locals())


def searchVuln(request):
    if request.method == "POST":
        activitee_parente = None
        form = SearchVulnForm(request.POST)
        if form.is_valid():
            vulnerabilite_list = []
            mot_clef = form.cleaned_data["mot_clef"]
            activitee_parente = form.cleaned_data["activites_liees"]
            desc = form.cleaned_data["recherche_dans_la_description_de_la_vuln"]
            vulnerabilite_list1 = Vulnerabilite.objects.filter(mots_clefs__nom__icontains=mot_clef, description__icontains=desc)
            for vuln in vulnerabilite_list1:
                for activite in vuln.activites_liees.all():
                    if activite.isEnfant(activitee_parente):
                        vulnerabilite_list.append(vuln)
                        break
        else:
            error_message = 'Votre requête contient des erreurs, veuillez réessayer svp.'
        form.updateActivites(activitee_parente)
        return render(request, 'home/vulnerabilite_list_body.html', locals())
    else:
        return redirect(reverse('home:index'))


def displayReco(request):
    recommandation_list = Recommandation.objects.all()
    form = SearchRecoForm()
    return render(request, 'home/recommandation_list.html', locals())


def searchReco(request):
    if request.method == "POST":
        form = SearchRecoForm(request.POST)
        if form.is_valid():
            expl = form.cleaned_data["recherche_dans_explication_reco"]
            recommandation_list = Recommandation.objects.filter(explication__icontains=expl)
        else:
            error_message = 'Votre requête contient des erreurs, veuillez réessayer svp.'
        return render(request, 'home/recommandation_list.html', locals())
    else:
        return redirect(reverse('home:recos'))
# coding: utf8
from django import forms
from .models import ActiviteAudit
from django.db.models import Q


class SearchVulnForm(forms.Form):
    # error_messages = {
    #     'mot_clef_vide': "Vous n'avez pas renseigné de mot-clef.",
    # }

    mot_clef = forms.CharField(label="Mot Clef", required=False)
    recherche_dans_la_description_de_la_vuln = forms.CharField(required=False)
    activites_liees = forms.ModelChoiceField(label="Activité d'audit correspondante", queryset=ActiviteAudit.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(SearchVulnForm, self).__init__(*args, **kwargs)
        self.fields['mot_clef'].widget.attrs\
            .update({
                'placeholder': "ex : XSS",
                'class': 'form-control',
                'autofocus': 'true',
            })
        self.fields['activites_liees'].widget.attrs\
            .update({
                'placeholder': "Activité d'audit correspondante à la vulnérabilité",
                'class': 'form-control',
            })
        self.fields['recherche_dans_la_description_de_la_vuln'].widget.attrs\
            .update({
                'placeholder': "ex : filtrage des données utilisateur",
                'class': 'form-control',
            })

    # def clean_mot_clef(self):
    #     mot_c = self.cleaned_data.get('mot_clef')
    #     if not mot_c:
    #         raise forms.ValidationError(
    #             self.error_messages['mot_clef_vide'],
    #             code='mot_clef_vide',
    #         )
    #     return mot_c

    def updateActivites(self, activite_parente = None):
        if activite_parente is None:
            self.fields['activites_liees'].queryset = ActiviteAudit.objects.filter(activiteParente=activite_parente)
        else:
            self.fields['activites_liees'].queryset = ActiviteAudit.objects.filter(Q(activiteParente=activite_parente) | Q(pk=activite_parente.id) )


class SearchRecoForm(forms.Form):

    recherche_dans_explication_reco = forms.CharField(label='Recherche dans l\'explication de la reco', required=False)

    def __init__(self, *args, **kwargs):
        super(SearchRecoForm, self).__init__(*args, **kwargs)
        self.fields['recherche_dans_explication_reco'].widget.attrs\
            .update({
                'placeholder': "ex : pour le php utilisez htmlentities",
                'class': 'form-control',
            })

# coding: utf8
from django import forms
from .models import ActiviteAudit
from django.db.models import Q


class SearchVulnForm(forms.Form):
    # error_messages = {
    #     'mot_clef_vide': "Vous n'avez pas renseigné de mot-clef.",
    # }

    dernier_index = 0
    index_modifie = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # mot_clef = forms.CharField(label="Mot Clef", required=False)
    mots_clefs = forms.CharField(widget=forms.HiddenInput(), required=False)
    recherche_dans_la_description_de_la_vuln = forms.CharField(required=False)
    # activites_liees = forms.ModelChoiceField(label="Activité d'audit correspondante", queryset=ActiviteAudit.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        activite_parente = kwargs.pop('activite_parente', None)
        super(SearchVulnForm, self).__init__(*args, **kwargs)
        # self.fields['mot_clef'].widget.attrs \
        #     .update({
        #         'placeholder': "ex : XSS",
        #         'class': 'form-control',
        #         'autofocus': 'true',
        #     })
        self.fields['recherche_dans_la_description_de_la_vuln'].widget.attrs \
            .update({
                'placeholder': "ex : filtrage des données utilisateur",
                'class': 'form-control',
            })
        # self.fields['activites_liees'].widget.attrs\
        #     .update({
        #         'placeholder': "Activité d'audit correspondante à la vulnérabilité",
        #         'class': 'form-control',
        #     })
        list_activites = []
        while activite_parente is not None:
            list_activites.append(activite_parente)
            activite_parente = activite_parente.activiteParente
        self.fields['activites_liees_0'] = \
            forms.ModelChoiceField(label="Activité d'audit correspondante",
                                   queryset=ActiviteAudit.objects.filter(activiteParente=None),
                                   required=False)
        self.fields['activites_liees_0'].widget.attrs \
            .update({
                'placeholder': "Activité d'audit correspondante à la vulnérabilité",
                'class': 'form-control',
            })
        if len(list_activites) != 0:
            for index, act in enumerate(reversed(list_activites)):
                query = ActiviteAudit.objects.filter(activiteParente=act)
                if query:
                    self.fields['activites_liees_{index}'.format(index=index+1)] = \
                        forms.ModelChoiceField(label="Activité d'audit correspondante",
                                               queryset=query,
                                               required=False)
                    self.fields['activites_liees_{index}'.format(index=index+1)].widget.attrs \
                        .update({
                            'placeholder': "Activité d'audit correspondante à la vulnérabilité",
                            'class': 'form-control',
                    })
                    self.dernier_index = index+1


    # def clean_mot_clef(self):
    #     mot_c = self.cleaned_data.get('mot_clef')
    #     if not mot_c:
    #         raise forms.ValidationError(
    #             self.error_messages['mot_clef_vide'],
    #             code='mot_clef_vide',
    #         )
    #     return mot_c


class SearchRecoForm(forms.Form):
    recherche_dans_explication_reco = forms.CharField(label='Recherche dans l\'explication de la reco', required=False)
    themes = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(SearchRecoForm, self).__init__(*args, **kwargs)
        self.fields['recherche_dans_explication_reco'].widget.attrs \
            .update({
            'placeholder': "ex : pour le php utilisez htmlentities",
            'class': 'form-control',
        })

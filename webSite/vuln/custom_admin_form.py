# coding: utf-8
from django import forms


class MyActiviteAuditAdminForm(forms.ModelForm):
    error_messages = {
        'boucle': "Cette activite ne peut pas avoir comme parent le choix demandé car c'est une de ses activités enfants.",
    }

    def clean_activiteParente(self):
        activite = self.cleaned_data["activiteParente"]
        if hasattr(self, 'instance') and self.instance.pk is not None:
            # update
            if activite and self.instance:
                if activite.isEnfant(self.instance):
                    raise forms.ValidationError(
                        self.error_messages['boucle'],
                        code='boucle',
                    )
        return activite


class MyMotClefAdminForm(forms.ModelForm):
    error_messages = {
        'caractere_interdit': "Le caractère '-' est interdit dsl.",
    }

    def clean_nom(self):
        nom = self.cleaned_data["nom"]
        if '-' in nom:
            raise forms.ValidationError(
                self.error_messages['caractere_interdit'],
                code='caractere_interdit',
            )
        return nom

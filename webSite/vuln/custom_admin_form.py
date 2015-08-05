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

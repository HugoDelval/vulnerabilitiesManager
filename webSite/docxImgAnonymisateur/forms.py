# coding: utf-8
import os
from django import forms


class DocxUploadFileForm(forms.Form):
    error_messages = {
        'empty_file': "Le type de fichier est vide. Veuillez uploader un fichier valide svp",
        'wrong_file': "Le type de fichier est invalide. Veuillez uploader un fichier de type Docx (Word)",
    }

    fichier = forms.FileField()
    niveau_de_flou = forms.IntegerField(max_value=50, min_value=5)

    def __init__(self, *args, **kwargs):
        super(DocxUploadFileForm, self).__init__(*args, **kwargs)
        self.fields['fichier'].widget.attrs\
            .update({
                'placeholder': "Fichier Docx à Anonymiser",
            })
        self.fields['niveau_de_flou'].widget.attrs\
            .update({
                'placeholder': "Rayon du flou",
                'class': 'form-control',
                'value': 17
            })

    def clean_fichier(self):
        fichier = self.cleaned_data.get('fichier')
        if not fichier:
            raise forms.ValidationError(
                self.error_messages['empty_file'],
                code='empty_file',
            )
        s = ''
        for b in fichier.chunks(10):
            s += b
        if not s.startswith("\x50\x4b\x03\x04"):
            raise forms.ValidationError(
                self.error_messages['wrong_file'],
                code='wrong_file',
            )
        return fichier

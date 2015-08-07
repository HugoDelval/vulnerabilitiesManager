# coding: utf-8
import os
from django import forms


class DocxUploadFileForm(forms.Form):
    error_messages = {
        'empty_file': "Le type de fichier est vide. Veuillez uploader un fichier valide svp",
        'wrong_file': "Le type de fichier est invalide. Veuillez uploader un fichier de type Docx (Word)",
        'txt_original_vide': "Le texte final ne peut être rempli qu'à condition que le texte original soit rempli !"
    }

    fichier = forms.FileField()
    niveau_de_flou = forms.IntegerField(max_value=50, min_value=5)

    texte_original = forms.CharField(required=False)
    texte_final = forms.CharField(required=False)
    extra_field_count = forms.IntegerField(widget=forms.HiddenInput())

    extra_fields = 0

    def __init__(self, *args, **kwargs):
        self.extra_fields = int(kwargs.pop('extra', '0'))
        super(DocxUploadFileForm, self).__init__(*args, **kwargs)

        self.fields['extra_field_count'].initial = self.extra_fields

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
        self.fields['texte_original'].widget.attrs\
            .update({
                'placeholder': "d'amossys",
                'class': 'form-control',
            })
        self.fields['texte_final'].widget.attrs\
            .update({
                'placeholder': "[du client]",
                'class': 'form-control',
            })

        for index in range(0, self.extra_fields):
            self.fields['extra_texte_original_{index}'.format(index=index)] = \
                forms.CharField(required=False)
            self.fields['extra_texte_original_{index}'.format(index=index)].widget.attrs\
                .update({
                    'placeholder': "amossys",
                    'class': 'form-control',
                })
            self.fields['extra_texte_final_{index}'.format(index=index)] = \
                forms.CharField(required=False)
            self.fields['extra_texte_final_{index}'.format(index=index)].widget.attrs\
                .update({
                    'placeholder': "[client]",
                    'class': 'form-control',
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

    def clean(self):
        erreur_txt_or = forms.ValidationError(
            self.error_messages['txt_original_vide'],
            code='txt_original_vide',
        )
        cleaned_data = super(DocxUploadFileForm, self).clean()
        texte_final = cleaned_data.get('texte_final')
        texte_original = cleaned_data.get('texte_original')
        if texte_final and not texte_original:
            self.add_error('texte_final', erreur_txt_or)
            raise erreur_txt_or
        for i in range(0, self.extra_fields):
            texte_final = cleaned_data.get('extra_texte_final_{index}'.format(index=i))
            texte_original = cleaned_data.get('extra_texte_original_{index}'.format(index=i))
            if texte_final and not texte_original:
                self.add_error('extra_texte_final_{index}'.format(index=i), erreur_txt_or)
                raise erreur_txt_or
        return cleaned_data

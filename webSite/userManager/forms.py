# coding: utf8
from django import forms

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Pseudo ou E-mail", max_length=50)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(ConnexionForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'placeholder': "Pseudo ou E-mail",
                'class': 'form-control'
            })
        self.fields['password'].widget.attrs\
            .update({
                'placeholder': "Mot de passe",
                'class': 'form-control'
            })


class ChangeMdpForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangeMdpForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs\
            .update({
                'placeholder': "Ancien mot de passe",
                'class': 'form-control'
            })
        self.fields['new_password1'].widget.attrs\
            .update({
                'placeholder': "Nouveau mot de passe",
                'class': 'form-control'
            })
        self.fields['new_password2'].widget.attrs\
            .update({
                'placeholder': "Repetition",
                'class': 'form-control'
            })
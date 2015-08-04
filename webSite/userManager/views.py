# coding: utf8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from .forms import ConnexionForm, InscriptionForm


@sensitive_post_parameters()
@csrf_protect
@never_cache
def connexion(request):
    if request.user.is_authenticated():
        return redirect(reverse('vuln:index'))
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Connexion via email
            if "@" in username:
                user_by_mail = User.objects.filter(email=username)
                if user_by_mail:
                    # username unique
                    if user_by_mail[0]:
                        username = user_by_mail[0].username

            user = authenticate(username=username, password=password)
            if user:    # != None
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('vuln:index'))
                else:
                    error = True
                    error_type = "inactive"
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'userManager/connexion.html', locals())


@login_required
def deconnexion(request):
    logout(request)
    return redirect(reverse('userManager:connexion'))

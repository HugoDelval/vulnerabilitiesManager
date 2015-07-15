from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse


def index(request):
    template_name='home/index.html'
    context = {
    }
    return render(request, template_name, context)


# def details(request,)
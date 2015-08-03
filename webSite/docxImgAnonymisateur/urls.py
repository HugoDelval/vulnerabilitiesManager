from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /anonymiser/
    url(r'^$', views.index, name='index'),
]
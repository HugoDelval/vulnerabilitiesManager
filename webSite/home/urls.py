from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', RedirectView.as_view(pattern_name='home:index', permanent=True)),
    # ex: vulns/
    url(r'^vulns/$', views.displayVuln, name='index'),
    # ex: vulns/search/
    url(r'^vulns/search/$', views.searchVuln, name='search_vuln'),
    # ex: recos/
    url(r'^recos/$', views.displayReco, name='recos'),
    # ex: recos/search/
    url(r'^recos/search/$', views.searchReco, name='search_reco'),
    # ex : vulns/detail/3/
    url(r'^vulns/detail/(?P<pk>[0-9]+)/$', views.VulnDetailView.as_view(), name='show_me_this_vuln'),
    # ex : recos/detail/3/
    url(r'^recos/detail/(?P<pk>[0-9]+)/$', views.RecoDetailView.as_view(), name='show_me_this_reco'),
]

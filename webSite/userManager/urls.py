from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /user/login
    url(r'^login', views.connexion, name='connexion'),
    # ex: /user/login
    url(r'^register', views.inscription, name='inscription'),
    # ex: /user/logout
    url(r'^logout', views.deconnexion, name='deconnexion'),
]
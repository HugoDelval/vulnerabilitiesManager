# vulnerabilitiesManager

## Installation et lancement

	sudo pip install django
	git clone https://github.com/HugoDelval/vulnerabilitiesManager/tree/master/webSite/vuln
	cd  vulnerabilitiesManager/webSite/webSite
	cp databases_example.py databases.py

Modifier le fichier databases.py en fonction de vos paramètres locaux de mysql.
N'oubliez pas de lancez mysql :

	sudo service mysql start

Vous serez peut-être amené à créer une base de données :

	CREATE DATABASE kmbdd;


	sudo apt-get install python-ldap
	sudo pip install django-auth-ldap
	sudo pip install django-grappelli
	sudo pip install django-extensions

	python manage.py migrate

Vous pouvez accéder à l'interface admin (pour ajouter des vulnérabilités/recommandations) en créant un administrateur :

	python manage.py createsuperuser

Puis lancez le server :

	python manage.py runserver 8081

ouvrez un navigateur et allez à localhost:8081 ou localhost:8081/admin pour l'interface admin

#### Générer une image de votre modèle de données

	sudo pip install pyparsing==1.5.7
	sudo pip install pydot

	python manage.py graph_models -g -o <NOM>.png <Application à partir de laquelle générer l'image du modèle>
	python manage.py graph_models -g -o diagramme.png vuln


## Developpement

Pour vous aider a créer un nouvelle application (*monApp*) sur le site voici quelques conseils :    
1. Créer l'application avec `python manage.py startapp monApp`  
2. Mettre *monApp* dans la variable `INSTALLED_APPS` pour l'ajouter au site dans le fichier **webSite/setting.py**  
3. Ajouter une route de base du type `url(r'^maroute/', include('monApp.urls', namespace='monApp'))` dans **siteWeb/urls.py**  
4. Développer *monApp*  
  
* *Pour les* **modèles** *:*  
 * Vous pouvez établir des relations avec les utilisateurs en définissant une clé étrangère sur la classe `User`, importés comme ceci : `from django.contrib.auth.models import User`  
 * Pour établir cette relation penser à nommer la relation inverse c'est plus pratique, comme ceci : `Class Vuln(models.Model):` puis `user = models.ForeignKey(User, related_name='mes_vulns')`  
 * Après avoir créé vos modèles (inspirez vous de **vuln/models.py**) vous devez lancez ces commandes pour synchroniser la bdd :

	> python manage.py makemigrations # importe les changements dans un cache qui peut être versionné (par git entre autre)

	> python manage.py migrate        # prend en compte les changements précédemment importés et les insère dans la bdd (mysql ici) 
 
* *Pour les* **vues** *(contrôleurs)* :  
  * Penser à ajouter le décorateur `@login_required` au dessus de vos actions, les utilisateurs déconnectés seront directement redirigés vers la page de connexion (pas encore développé avec le ldap d'Amossys)  
  * Ajouter une route vers votre action et nommez la dans **monApp/urls.py** (créez le fichier si besoin) comme ceci : `urlpatterns = [ url(r'^', views.index, name='index'),]`  
  
* *Pour les* **templates** *:*  
  * Copier le fichier **LTE/templates/LTE/starter.html**, et le renommer en **layout.html** dans **monApp/templates/monApp/**  
  * Adapter et redéfinir tout les blocks du **layout.html** pour *monApp*  
  * Ce fichier **layout.html** sera la base de votre application, toute vos pages seront basées dessus  
  * Creer maintenant un *nouveau* template basé sur le fichier **LTE/templates/LTE/page.html**   
  * Faire donc hériter le nouveau template de **monApp/templates/monApp/layout.html**   
  * Modifier le contenu de ce fichier pour qu'il corresponde à votre page   
  * *C'est bon !* Le templating en 3 couches (Base / Layout / Page) est terminé ! 
  * Si vous utilisez de l'**AJAX** passez par l'app ajax qui centralise ces requetes. Un **jeton csrf** est obligatoire même en ajax ! Infos [ici](https://docs.djangoproject.com/fr/1.7/ref/contrib/csrf/#csrf-ajax).   

## Sources et remerciements
https://github.com/SpamNocturne/SpamWeb

# vulnerabilitiesManager

## Installation Linux

	sudo pip install django
	git clone https://github.com/HugoDelval/vulnerabilitiesManager/tree/master/webSite/vuln
	cd  vulnerabilitiesManager/webSite/webSite
	cp databases_example.py databases.py

Modifier le fichier databases.py en fonction de vos paramètres locaux de mysql.
N'oubliez pas de lancez mysql :

	sudo service mysql start

Créer une base de données :

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

## Installation Windows

Installer votre windows server 2012 R2 et faites vos mises à jour (panneau de configuration>windows update).

Assurer vous que la machine possède une adresse IP fixe.

Lors de l'installation ne pas hésiter à redémarrer le serveur après chaque installation.

### MySQL

Installer MySQL via le site officiel. Note : il est possible que vous ayez à installer Visual C++ 2013 également

Ajouter une table : kmbdd

Ajouter un utilisateur dont les droits seront réduits à cette table

### Code source

Télécharger le code source du site KMAmossys. Disponible sur github : https://github.com/HugoDelval/vulnerabilitiesManager

### IIS - installation et configuration

Ouvrir le gestionnaire du serveur et ajouter des rôles et fonctionnalités :
	- Ajouter IIS (serveur WEB) avec *CGI*
	- Ajouter à IIS le service de rôle *Securité > Authentification Windows*

Ouvrir IIS et supprimer le site par default. Refermer IIS

Installer Web Platform Installer : 
http://www.microsoft.com/web/downloads/platform.aspx

Lancer WPI *en tant qu'admin* et dans options (en bas) *Flux Personnalisés* ajouter http://www.helicontech.com/zoo/feed.xml (selectionner IIS et pas IIS express) puis valider.

Ajouter *Zoo > Template > Python Project* puis Installer (en bas à droite).

Site Web : Nouveau site Web

Nom : KMAmossys

Chemin d'accès : le chemin vers un nouveau dossier, ce sera la racine de votre site. Ex: C:\www

Ouvrir IIS et lancer le site nouvellement créé. Ouvrir IE et aller sur *localhost*

Si tout a bien fonctionné dans C:\www\ il devrait y avoir un fichier nommé deploy_done.py (et non deploy.py, si c'est le cas assurez-vous que vous avez bien accédé le bon site IIS)

Ouvrir C:\www\static\zoo-index.html#existing-django-app

Executer les actions spécifiées dans le paragraphe en remplaçant *myproject1* par *webSite* et *settings* par *webSite.settings*

Ajouter C:\Python27\ et C:\Python27\Scripts\ au path

Ajouter le répertoire virtuel static : clic droit sur le site > ajouter un répertoire virtuel > static, pointe vers le répertoire static du code source téléchargé

Changer STATIC_ROOT dans webSite/settings.py en qqchose du genre *C:\\www\\static*

Ouvrir une cmd.exe dans le répertoire racine de l'appli (C:\www) :

	pip install django

	pip install django-grappelli

	pip install django-extensions

	pip uninstall Pillow

	pip install Pillow

	pip install pyparsing==1.5.7

	pip install pydot

	python manage.py collectstatic

Créer un fichier secret_key.txt accessible par IIS (donc dans C:\\www par exemple) contenant une ligne qui sera une clef pour django (donc il faut qu'elle soit complexe)

Modifier la ligne 23 de settings.py pour donner le chemin vers le fichier créé

#### HTTPs

Cliquer sur le serveur pui sur *Certificats de serveur*

A droite cliquer sur *Créer un certificat auto-signé*

Clic droit sur le site > Liaisons > Ajouter > HTTPs + Certificat que vous venez de créer > OK

#### 1ere magouille

Ceci est une note au développeur. Il semblait nécessaire de forcer le chargement des paramètres django, l'application ne le faisait pas automatiquement. On obtenait l'erreur suivante : **Models aren't loaded yet**

Ainsi nous avons rajouté la ligne *django.setup()* dans le fichier *webSite/urls.py*

#### Test partie Django - IIS

Cliquer sur le site > Authentification > clic droit sur **Authentification anonyme** > Modifier > Identité du pool d'application

A ce stade le site fonctionne (normalement). Arreter le serveur puis relancer le et faire de même pour le site web. Aller ensuite sur localhost via IE. Si vous voyez une page de conexion alors parfait, sinon débugguer.

Source : http://www.helicontech.com/articles/running-django-on-windows-with-performance-tests/

#### IIS - Active Directory

La suite est un test d'authentification*Kerberos* qui a été monté en local. Tou n'est donc pas à prendre (vous pouvez ignorer la création de l'AD par exemple)

Creer un AD en rajoutant un rôle au serveur. Creer une foret (HUGO.AD ici). Ajouter un serveur DNS

Ouvrir le centre d'administration de active director. HUGO > Domain Controllers > double clic sur le serveur > Délégation > Approuver délégation Kerberos

Cliquer sur le site > Authentification > désactiver authentification anonyme > activer authentification windows

Authentification Windows > Paramètres avancés > désactiver l'authentification du mode noyau

Authentification Windows > Fournisseurs > Supprimer tout et ne mettre que *Negotiate:Kerberos*

#### 2nde magouille

A ce stade l'authentification devrait être opérationnelle. Cependant on veut que toutes les personnes se connectant en remote user aient accès à l'interface admin. Pour ce faire on va modifier le comportement par défaut de django :

Ouvrir le fichier C:\Python27\Lib\site-packages\django\contrib\auth\models.py

Modifier l'attribut is_superuser de PermissionMixin ligne 308 : changer **default=False** en **default=True**

Modifier l'attribut is_staff de AbstractUser ligne 400 : changer **default=False** en **default=True**

Ainsi les comptes créés automatiquement lors de la connexion via KERBEROS seront des comptes administrateur.

#### export modèle et base de données

Ouvrir un cmd.exe dans le répertoire C:\www et executer :

	python manage.py migrate

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

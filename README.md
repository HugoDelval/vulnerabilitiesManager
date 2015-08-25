# vulnerabilitiesManager

## Installation Linux - partie 1 - branche master

La branche *master* est la branche qui correspond au développement de l'application, elle est utilisée dans cette 1ère partie pour débugguer plus facilement les éventuels problèmes de déploiements.

	git clone https://github.com/HugoDelval/vulnerabilitiesManager

	cd  vulnerabilitiesManager/webSite/webSite

	git checkout master

	cp databases_example.py databases.py

Lancer mysql :

	sudo service mysql start

Créer une base de données :

	CREATE DATABASE kmbdd;

Modifier le fichier databases.py en fonction de vos paramètres locaux de mysql. NB: Pensez à créer un utilisateur ayant des droits restreints à cette BdD.

Installer les dépendances :

	sudo pip install django

	sudo pip install django-grappelli

	sudo pip install django-extensions

	sudo pip uninstall Pillow

	sudo pip install Pillow

	sudo pip install pyparsing==1.5.7

	sudo pip install pydot

Commande permettant de contruire le shéma de la base de données mysql (dossier racine) :

	python manage.py migrate

Vous pouvez accéder à l'interface admin (pour ajouter des vulnérabilités/recommandations) en créant un administrateur :

	python manage.py createsuperuser

Lancer le serveur de développement :

	python manage.py runserver 8081

Ouvrir un navigateur et allez à l'URL http://localhost:8081 ou http://localhost:8081/admin pour l'interface admin

#### Générer une image de votre modèle de données

	python manage.py graph_models -g -o <NOM>.png <Application à partir de laquelle générer l'image du modèle>

	python manage.py graph_models -g -o diagramme.png vuln

## Installation Linux - partie 2

Si vous êtes arrivés jusqu'ici alors l'application est fonctionnelle sous votre machine. Il ne vous reste plus qu'à la mettre en production. Ceci signifie entre autre :

	- Passer sous la branche de production
	- Déléguer la gestion du serveur à Apache plutôt qu'au serveur de développement de la section précédente
	- Activer une connexion HTTPs
	- Durcir les paramètres de l'application (utilisation de Cookies HTTPOnly, configuration de la clef secrete de Django etc..)

### Branche de production

Passer sous la branche de production du projet KMAmossys :

	git checkout production

Ceci permet de charger les paramètres durcis de Django. Le fichier qui a le plus changé entre la branche **master** et la branche **production** est le fichier **webSite/webSite/settings.py**. Dans ce fichier vous trouverez tous les paramètres de Django. Voici un peu de documentation officielle en cas de problème (ou de curieux) :
https://docs.djangoproject.com/en/1.8/topics/settings/

*Note:* La documentation Django est très complète et bien expliquée pour des débutants. N'hésitez pas à vous y référer régulièrement.

### Apache et Python

Installer le module python d'Apache :

	sudo apt-get install libapache2-mod-wsgi

Voici la documentation officielle du déploiement sous Apache : https://docs.djangoproject.com/fr/1.8/howto/deployment/wsgi/modwsgi/

Activer le module python Apache :

	sudo a2enmod wsgi

Déclarer l'application Python dans Apache :
ouvrir le fichier **/etc/apache2/apache2.conf** (avec les droits *root*) et insérer les lignes suivantes à la suite des directives *\<Directory\>\</Directory\>* :


	Alias /static/ /home/hdl/KM/vulnerabilitiesManager/webSite/static/

	<Directory /home/hdl/KM/vulnerabilitiesManager/webSite/static>
	Require all granted
	</Directory>


	WSGIScriptAlias / /home/hdl/KM/vulnerabilitiesManager/webSite/webSite/wsgi.py
	WSGIPythonPath /home/hdl/KM/vulnerabilitiesManager/webSite/

	<Directory /home/hdl/KM/vulnerabilitiesManager/webSite>
	<Files wsgi.py>
	Require all granted
	</Files>
	</Directory>

Attention ! Changer le répertoire **/home/hdl/KM/vulnerabilitiesManager** en fonction de votre installation locale !

### Activation du HTTPs

La source utilisée pour l'activation du HTTPs sous apache2 : http://www.it-connect.fr/configurer-le-ssl-avec-apache-2%EF%BB%BF/

L'activation du HTTPs n'est pas spécifique à Django, de nombreuses ressources sont disponibles sur le WEB.

Résumé :

Activer le site SSL ainsi que le module SSL :

	sudo a2enmod ssl

	sudo a2ensite default-ssl

	sudo service apache2 reload

*Optionnel*

Editer le fichier **/etc/apache2/sites-available/default-ssl.conf** (avec les droits admin) :

	SSLCertificateFile /chemin/server.crt # le chemin du certificat que vous avez créé, sinon le chemin vers le certificat généré automatiquemennt à l'installation

	SSLCertificateKeyFile /chemin/server.key # idem, la clef que vous avez créée, ou bien la clef d'apache générée automatiquement

D'autres paramètres que vous pouvez changer dans ce fichier (pour plus de sécurité SSL) :

	SSLProtocol -ALL +TLSv1 +TLSv1.1 +TLSv1.2

	SSLHonorCipherOrder On

	SSLCipherSuite ECDHE-RSA-AES128-SHA256:AES128-GCM-SHA256:HIGH:!MD5:!aNULL:!EDH:!RC4

	SSLCompression off

Relancer apache :

	sudo service apache2 reload

*Fin optionnel*

#### Redirection HTTP - HTTPs :

La redirection se fait déjà au niveau de l'application Django, mais cela ne coûte rien de la faire au niveau d'Apache également :

Editer le fichier **/etc/apache2/sites-available/000-default.conf** et rajouter cette ligne après **<VirtualHost *:80>**:

	Redirect permanent / https://{Inserer ici votre adresse IP}/

### Durcicement des paramètres de sécurité

Nous avons déjà parlé du fichier de configuration Django : **webSite/webSite/settings.py**.
Ouvrir ce fichier. Changer la ligne suivante :

	** with open('/etc/secret_key.txt') as f: **

Avec le fichier qui contiendra votre clef privée Django. Ce fichier contient une unique ligne du style :

	kjodsf!:;ç_è986442654/*.CKSQJUBHiusbdkJBIBSGLnSMJSBIGi!:.;PQOKGFM§S.Goisgugs><<qd

Changer également la ligne qui correspond au chemin absolu vers tous les fichiers statiques (css, images, javascript..) :

	STATIC_ROOT = '/home/hdl/KM/vulnerabilitiesManager/webSite/static/'

	ex : STATIC_ROOT = '/home/audit/KM/vulnerabilitiesManager/webSite/static/'

Changer les droits POSIX pour l'upload de fichier :

	sudo chown :www-data webSite/docxImgAnonymisateur/includes/doc_a_anonymiser -R

	sudo chmod 664 webSite/docxImgAnonymisateur/includes/doc_a_anonymiser

	sudo chown :www-data webSite/docxImgAnonymisateur/includes/doc_anonyme -R

	sudo chmod 664 webSite/docxImgAnonymisateur/includes/doc_anonyme

L'installation est presque terminée ! Lisez la partie suivante pour comprendre les bases de Django, nottament la migration de la base de données.

## Découverte de Django



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

Chemin d'accès : le chemin vers un nouveau dossier, ce sera la racine de votre site. Ex: C:/www

Ouvrir IIS et lancer le site nouvellement créé. Ouvrir IE et aller sur *localhost*

Si tout a bien fonctionné dans C:/www/ il devrait y avoir un fichier nommé deploy_done.py (et non deploy.py, si c'est le cas assurez-vous que vous avez bien accédé le bon site IIS)

Ouvrir C:/www/static/zoo-index.html#existing-django-app

Executer les actions spécifiées dans le paragraphe en remplaçant *myproject1* par *webSite* et *settings* par *webSite.settings*

Ajouter C:/Python27/ et C:/Python27/Scripts/ au path

Ajouter le répertoire virtuel static : clic droit sur le site > ajouter un répertoire virtuel > static, pointe vers le répertoire static du code source téléchargé

Changer STATIC_ROOT dans webSite/settings.py en qqchose du genre *C:/www/static*

Ouvrir une cmd.exe dans le répertoire racine de l'appli (C:/www) :

	pip install django

	pip install django-grappelli

	pip install django-extensions

	pip uninstall Pillow

	pip install Pillow

	pip install pyparsing==1.5.7

	pip install pydot

	python manage.py collectstatic

Créer un fichier secret_key.txt accessible par IIS (donc dans C:/www par exemple) contenant une ligne qui sera une clef pour django (donc il faut qu'elle soit complexe)

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

Ouvrir le fichier C:/Python27/Lib/site-packages/django/contrib/auth/models.py

Modifier l'attribut is_superuser de PermissionMixin ligne 308 : changer **default=False** en **default=True**

Modifier l'attribut is_staff de AbstractUser ligne 400 : changer **default=False** en **default=True**

Ainsi les comptes créés automatiquement lors de la connexion via KERBEROS seront des comptes administrateur.

#### export modèle et base de données

Ouvrir un cmd.exe dans le répertoire C:/www et executer :

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

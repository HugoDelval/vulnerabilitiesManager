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

	mysql> CREATE DATABASE kmbdd;

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

Ouvrir un navigateur et allez à l'URL http://localhost:8081 ou http://localhost:8081/admin pour l'interface admin. Les login et mot de passe sont ceux du superuser que vous venez de créer.

## Installation Linux - partie 2

Si vous êtes arrivés jusqu'ici alors l'application est fonctionnelle sous votre machine. Il ne vous reste plus qu'à la mettre en production. Ceci signifie entre autre :

	* Passer sous la branche de production
	* Déléguer la gestion du serveur à Apache plutôt qu'au serveur de développement de la section précédente
	* Activer une connexion HTTPs
	* Durcir les paramètres de l'application (utilisation de Cookies HTTPOnly, configuration de la clef secrete de Django etc..)

### Branche de production

Passer sous la branche de production du projet KMAmossys :

	git checkout production

Ceci permet de charger les paramètres durcis de Django. Le fichier qui a le plus changé entre la branche **master** et la branche **production** est le fichier **webSite/webSite/settings.py**. Dans ce fichier vous trouverez tous les paramètres de Django. Voici un peu de documentation officielle en cas de problème (ou de curiosité) :
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

Editer le fichier **/etc/apache2/sites-available/000-default.conf** et rajouter cette ligne après **\<VirtualHost \*:80\>**:

	Redirect permanent / https://{Inserer ici votre adresse IP}/

### Durcicement des paramètres de sécurité

Nous avons déjà parlé du fichier de configuration Django : **webSite/webSite/settings.py**.
Ouvrir ce fichier. Changer la ligne suivante :...

	with open('/etc/secret_key.txt') as f:

... avec le fichier qui contiendra votre clef privée Django. Ce fichier contient une unique ligne du style :

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

### manage.py - l'outil d'administration

Encore une fois pour plus de précision : https://docs.djangoproject.com/fr/1.8/ref/django-admin/

Commande pour regrouper tous les fichiers statiques (CSS, JS, images..) dans le même dossier **/static/** :

	python manage.py collectstatic

Si vous mettez à jour des fichiers statiques il vous faudra executer cette commande ! Il est possible de supprimer entièrement le dossier **static**, cette commande le recontruira.

Commande pour charger les modèles (les objets) et les transformer en requêtes SQL :

	python manage.py makemigrations

Cette commande parse tous les fichiers appli/models.py (par exemple vuln/models.py) et transforme les objets en relations SQL. Ces relations sont stockées dans le dossier appli/migrations sous la forme de fichiers python. Ceci permet à ces migrations d'être versionnables (via git par exemple).

Commande pour appliquer ces migrations à la base de données :

	python manage.py migrate

Ceci éxécute les requêtes SQL générées avec **makemigrations**, et va donc créer les tables correspondants au modèle de données de appli/models.py

*Pocédure de récupération de la base de données depuis un backup :*

	mysql> CREATE DATABASE kmbdd;

	$> mysql -uamossys -pMOTDEPASSE -Dkmbdd < FICHIER_BACKUP.sql

	$> python manage.py migrate --fake #permet d'enregistrer les migrations pour ne pas qu'elles soient executées plus tard, mais sans executer les commandes SQL (--fake) puisque l'on vient de recontruire la base de données

Pour une utilisation "classique" de **migrate** et **makemigrations**, cf la partie Développement.

### Utilisation de KMAmossys

Dans cette partie nous expliquons à l'auditeur comment se servir de l'application (sans se soucier du code).
# TODO


### Developpement

#### La structure des fichiers de Django

Commençons à la racine du projet (le premier répertoire webSite/).

Nous pouvons déjà voir le dossier **static** dans lequel sont stockés toutes les resources images, JS, CSS (cf manage.py ci-dessus).

Nous avons ensuite le dossier **webSite** qui porte le même nom que notre projet (le dossier racine). Ce dossier est en fait construit à la création du projet et contient les éléments de base d'un projet : le serveur Django integré (fichier **webSite/wsgi.py**), les paramètres de projet (fichier **webSite/settings.py**), le fichier de routage initial (**webSite/urls.py**). Nous reviendrons à ces deux derniers fichiers par la suite.

Nous avons également le fichier **manage.py** de la section précédente. Ce fichier n'est utile que pour l'administration du site (création de nouveaux modèles, ajout de fichiers static etc..).

Chacun des autres dossiers correspond à une **application** de KMAmossys. Cette application a un rôle bien précis ce qui permet de séparer les fonctionnalités du site Web. Par exemple l'application userManager gère les utilisateur, notamment leur connexion.

La structure d'une application Django respecte l'architecture Modèle/Vues/Controleurs. Prenons l'exemple de l'application **vuln** qui gère la base de connaissance vulnérabilités / recommandations :

##### Modèles - Models

Les modèles sont stockés dans le fichier **vuln/models.py**.

Un modèle représente une entité de la vie courante que l'on modélise par une classe. On peut définir le type des attributs de cette classe (ex : *models.IntegerField()* est un entier). Vous pouvez également mettre en place des relations entre les modèles (correspondance avec les clefs étrangères de sql). Vous pouvez par exemple voir dans l'objet *Vulnerabilite* qu'une Vulnérabilité est liée à plusieurs mots clefs grâce à ce champ :

	**mots_clefs = models.ManyToManyField(MotClef)**

##### Vues - Templates

Les Vues (ou templates en anglais) sont dans le répertoire **vuln/templates/vuln/**.

Une Vue est appelée par le controlleur (section suivante) avec tous les paramètres nécessaires, par exemple les Vulnerabilités (ou d'autres objets) à afficher. La Vue se charge alors d'afficher ces objets via du HTML.

Dans la Vue on peut aussi rencontrer un langage de templating. Ce langage permet de parcourir facilement les arguments que nous a envoyé le controlleur (section suivante), en faisant des boucles ou des conditions. Ce langage est destiné à être très facilement appris et est donc très proche de la langue courante mais également limité en fonctionnalité.

##### Controlleurs - Views

Les controlleurs (ou views en anglais) sont présents dans le fichier **vuln/models.py**.

Chaque fonction dans ce fichier correspond à une action. Une View va être appelé par l'utilisateur, elle parse sa requête et récupère les modèles que souhaite l'utilisateur. Une fois toutes les données néssaires à l'affichage la View envoie ces Models au Template pour qu'il puisse les afficher.

##### Routage

Le fichier **vuln/urls.py** définit quels controlleurs sont appelés en fonction de l'URL demandé par l'utilisateur. 

#### Un exemple pour mieux comprendre

Pour que le rôle de chaque fichier soit plus clair, nous allons prendre un exemple. L'utilisateur demande l'URL /

Premièrement le projet charge les paramètres du projet depuis **webSite/settings.py** et cherche (entre autre) *ROOT_URLCONF = 'webSite.urls'*

Si on ouvre **webSite/urls.py** on voit que l'URL / est associée à une redirection vers **vuln:index**. 

On ouvre donc le fichier **vuln/urls.py** et on se rend compte que l'url **vuln:index** correspond à l'URL "/vulns/". En fait cette url (**vuln:index**) est un alias pour la véritable URL. ceci permet de rendre le code plus maintenable et plus propre.

L'URL ne correspond d'ailleurs pas à "/vulns/" mais en réalité à "/vuln/vulns/" car on est dans le sous dossier **vuln**.

On constate (toujours dans **vuln/urls.py**) que l'URL en question possède en 2nd paramètre la chaîne **views.displayVuln**. Ce qui signifie que le controlleur appelé est la fonction **displayVuln** du fichier **views.py** (le fichier des controlleurs).

Pour résumer la première étape : *l'utilisateur demande "/" => webSite.urls le redirige vers /vuln/vulns/ (défini dans vuln.urls) qui appelle la fonction views.displayVuln*

On ouvre maintenant le fichier **vuln/views.py** et on s'intéresse à la fonction displayVuln(). Cette fonction récupère toutes les vulnérabilités et les mots clefs. Elle créé également un formulaire (le formulaire de recherche) puis envoie le tout au template **vuln/vulnerabilite_list.html**

On ouvre donc le template **vuln/templates/vuln/vulnerabilite_list.html** et on observe que d'autres templates sont inclus dans celui-ci. L'affichage se fait par couche au niveau du template car ceci est plus simple à manipuler. On remarque entre autre l'insertion du template **vuln/vulnerabilite_list_body.html**. Si on l'ouvre on peut (enfin) observer l'affichage du formulaire de reche, ainsi que en bas l'affichage, via une boucle, des vulnérabilités récupérées préalablement dans la View.

#### Ajout d'un champ à l'objet **Recommandation**

#### Générer une image de votre modèle de données

	python manage.py graph_models -g -o <NOM>.png <Application à partir de laquelle générer l'image du modèle>

	python manage.py graph_models -g -o diagramme.png vuln

#### Création d'une nouvelle application

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

Cliquer sur le serveur puis sur *Certificats de serveur*

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

## Sources et remerciements
https://github.com/SpamNocturne/SpamWeb

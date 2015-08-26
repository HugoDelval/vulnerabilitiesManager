# Installation de KMAmossys sur une plateforme Linux

## Installation Linux - partie 1 - branche master

La branche **master** est la branche qui correspond au développement de l'application, elle est utilisée dans cette 1ère partie pour débugguer plus facilement les éventuels problèmes de déploiements.

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

Commande permettant de contruire le shéma de la base de données mysql (dossier racine : 1er dossier *webSite*) :

	python manage.py migrate

Vous pouvez accéder à l'interface admin (pour ajouter des vulnérabilités/recommandations) en créant un administrateur :

	python manage.py createsuperuser

Lancer le serveur de développement :

	python manage.py runserver 8081

Ouvrir un navigateur et allez à l'URL http://localhost:8081 ou http://localhost:8081/admin pour l'interface admin. Les login et mot de passe sont ceux du superuser que vous venez de créer.

## Installation Linux - partie 2

Si vous êtes arrivés jusqu'ici alors l'application est fonctionnelle sous votre machine. Il ne vous reste plus qu'à la mettre en production. Ceci signifie entre autre :

	** Passer sous la branche de production
	** Déléguer la gestion du serveur à Apache plutôt qu'au serveur de développement de la section précédente
	** Activer une connexion HTTPs
	** Durcir les paramètres de l'application (utilisation de Cookies HTTPOnly, configuration de la clef secrete de Django etc..)

### Branche de production

Passer sous la branche de production du projet KMAmossys :

	git checkout production

Ceci permet de charger les paramètres durcis de Django. Le fichier qui a le plus changé entre la branche *master* et la branche *production* est le fichier *webSite/webSite/settings.py*. Dans ce fichier vous trouverez tous les paramètres de Django. Voici un peu de documentation officielle en cas de problème (ou de curiosité) :
https://docs.djangoproject.com/en/1.8/topics/settings/

**Note:** La documentation Django est très complète et bien expliquée pour des débutants. N'hésitez pas à vous y référer régulièrement.

Une fois la branche changée il est **fortement conseillé** de copier le répertoire *webSite* dans un autre répertoire que celui actuel. Ainsi le répertoire ne sera plus versionné par git et aucun changement accidentel ne sera effectué (dû à un reboot de la machine par exemple).

### Apache et Python

Installer le module python d'Apache :

	sudo apt-get install libapache2-mod-wsgi

Voici la documentation officielle du déploiement sous Apache : https://docs.djangoproject.com/fr/1.8/howto/deployment/wsgi/modwsgi/

Activer le module python Apache :

	sudo a2enmod wsgi

Déclarer l'application Python dans Apache :
ouvrir le fichier */etc/apache2/apache2.conf* (avec les droits **root**) et insérer les lignes suivantes à la suite des directives **\<Directory\>\</Directory\>** :


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

Attention ! Changer le répertoire */home/hdl/KM/vulnerabilitiesManager* en fonction de votre installation locale !

### Activation du HTTPs

La source utilisée pour l'activation du HTTPs sous apache2 : http://www.it-connect.fr/configurer-le-ssl-avec-apache-2%EF%BB%BF/

L'activation du HTTPs n'est pas spécifique à Django, de nombreuses ressources sont disponibles sur le WEB.

Résumé :

Activer le site SSL ainsi que le module SSL :

	sudo a2enmod ssl

	sudo a2ensite default-ssl

	sudo service apache2 reload

**Optionnel**

Editer le fichier */etc/apache2/sites-available/default-ssl.conf* (avec les droits admin) :

	SSLCertificateFile /chemin/server.crt # le chemin du certificat que vous avez créé, sinon le chemin vers le certificat généré automatiquemennt à l'installation

	SSLCertificateKeyFile /chemin/server.key # idem, la clef que vous avez créée, ou bien la clef d'apache générée automatiquement

D'autres paramètres que vous pouvez changer dans ce fichier (pour plus de sécurité SSL) :

	SSLProtocol -ALL +TLSv1 +TLSv1.1 +TLSv1.2

	SSLHonorCipherOrder On

	SSLCipherSuite ECDHE-RSA-AES128-SHA256:AES128-GCM-SHA256:HIGH:!MD5:!aNULL:!EDH:!RC4

	SSLCompression off

Relancer apache :

	sudo service apache2 reload

**Fin optionnel**

#### Redirection HTTP - HTTPs :

La redirection se fait déjà au niveau de l'application Django, mais cela ne coûte rien de la faire au niveau d'Apache également :

Editer le fichier */etc/apache2/sites-available/000-default.conf* et rajouter cette ligne après *\<VirtualHost \**:80\>*:

	Redirect permanent / https://{Inserer ici votre adresse IP}/

### Durcicement des paramètres de sécurité

Nous avons déjà parlé du fichier de configuration Django : *webSite/webSite/settings.py*.
Ouvrir ce fichier. Changer la ligne suivante :...

	with open('/etc/secret_key.txt') as f:

... avec le fichier qui contiendra votre clef privée Django. Ce fichier contient une unique ligne du style :

	kjodsf!:;ç_è986442654/**.CKSQJUBHiusbdkJBIBSGLnSMJSBIGi!:.;PQOKGFM§S.Goisgugs><<qd

Changer également la ligne qui correspond au chemin absolu vers tous les fichiers statiques (css, images, javascript..) :

	STATIC_ROOT = '/home/hdl/KM/vulnerabilitiesManager/webSite/static/'

	ex : STATIC_ROOT = '/home/audit/KM/vulnerabilitiesManager/webSite/static/'

Changer les droits POSIX pour l'upload de fichier :

	sudo chown :www-data webSite/docxImgAnonymisateur/includes/doc_a_anonymiser -R

	sudo chmod 775 webSite/docxImgAnonymisateur/includes/doc_a_anonymiser

	sudo chown :www-data webSite/docxImgAnonymisateur/includes/doc_anonyme -R

	sudo chmod 775 webSite/docxImgAnonymisateur/includes/doc_anonyme

L'installation est presque terminée ! Lisez la partie suivante pour comprendre les bases de Django, nottament la migration de la base de données.

### manage.py - l'outil d'administration

Encore une fois pour plus de précision : https://docs.djangoproject.com/fr/1.8/ref/django-admin/

Commande pour regrouper tous les fichiers statiques (CSS, JS, images..) dans le même dossier */static/* :

	python manage.py collectstatic

Si vous mettez à jour des fichiers statiques il vous faudra executer cette commande ! Il est possible de supprimer entièrement le dossier *static*, cette commande le recontruira.

Commande pour charger les modèles (les objets) et les transformer en requêtes SQL :

	python manage.py makemigrations

Cette commande parse tous les fichiers appli/models.py (par exemple vuln/models.py) et transforme les objets en relations SQL. Ces relations sont stockées dans le dossier appli/migrations sous la forme de fichiers python. Ceci permet à ces migrations d'être versionnables (via git par exemple).

Commande pour appliquer ces migrations à la base de données :

	python manage.py migrate

Ceci éxécute les requêtes SQL générées avec *makemigrations*, et va donc créer les tables correspondants au modèle de données de appli/models.py

**Procédure de récupération de la base de données depuis un backup :**

	mysql> CREATE DATABASE kmbdd;

	$> mysql -uamossys -pMOTDEPASSE -Dkmbdd < FICHIER_BACKUP.sql

	$> python manage.py migrate --fake #permet d'enregistrer les migrations pour ne pas qu'elles soient executées plus tard, mais sans executer les commandes SQL (--fake) puisque l'on vient de recontruire la base de données

Pour une utilisation "classique" de *migrate* et *makemigrations*, cf la partie Développement.

**Commande mysql pour générer le backup utilisé ci-dessus : **

	mysqldump --opt -uUTILISATEUR -pMOT_DE_PASSE kmbdd > /home/hdl/KM/Backups_vulnmanager/backup_$(date +\%s).sql

Vous pouvez utiliser cette commande dans un cronjob par exemple.

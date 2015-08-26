# Installation de KMAmossys sur une plateforme Windows

Installer votre windows server 2012 R2 et faites vos mises à jour (panneau de configuration>windows update).

Assurer vous que la machine possède une adresse IP fixe.

Lors de l'installation ne pas hésiter à redémarrer le serveur après chaque installation.

## MySQL

Installer MySQL via le site officiel. Note : il est possible que vous ayez à installer Visual C++ 2013 également

Ajouter une table : kmbdd

Ajouter un utilisateur dont les droits seront réduits à cette table

## Code source

Télécharger le code source du site KMAmossys. Disponible sur github : https://github.com/HugoDelval/vulnerabilitiesManager

## IIS - installation et configuration

Ouvrir le gestionnaire du serveur et ajouter des rôles et fonctionnalités :
	- Ajouter IIS (serveur WEB) avec **CGI**
	- Ajouter à IIS le service de rôle **Securité > Authentification Windows**

Ouvrir IIS et supprimer le site par default. Refermer IIS

Installer Web Platform Installer : 
http://www.microsoft.com/web/downloads/platform.aspx

Lancer WPI **en tant qu'admin** et dans options (en bas) **Flux Personnalisés** ajouter http://www.helicontech.com/zoo/feed.xml (selectionner IIS et pas IIS express) puis valider.

Ajouter **Zoo > Template > Python Project** puis Installer (en bas à droite).

Site Web : Nouveau site Web

Nom : KMAmossys

Chemin d'accès : le chemin vers un nouveau dossier, ce sera la racine de votre site. Ex: C:/www

Ouvrir IIS et lancer le site nouvellement créé. Ouvrir IE et aller sur **localhost**

Si tout a bien fonctionné dans C:/www/ il devrait y avoir un fichier nommé deploy_done.py (et non deploy.py, si c'est le cas assurez-vous que vous avez bien accédé le bon site IIS)

Ouvrir C:/www/static/zoo-index.html#existing-django-app

Executer les actions spécifiées dans le paragraphe en remplaçant **myproject1** par **webSite** et **settings** par **webSite.settings**

Ajouter C:/Python27/ et C:/Python27/Scripts/ au path

Ajouter le répertoire virtuel static : clic droit sur le site > ajouter un répertoire virtuel > static, pointe vers le répertoire static du code source téléchargé

Changer STATIC_ROOT dans webSite/settings.py en qqchose du genre **C:/www/static**

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

### HTTPs

Cliquer sur le serveur puis sur **Certificats de serveur**

A droite cliquer sur **Créer un certificat auto-signé**

Clic droit sur le site > Liaisons > Ajouter > HTTPs + Certificat que vous venez de créer > OK

### 1ere magouille

Ceci est une note au développeur. Il semblait nécessaire de forcer le chargement des paramètres django, l'application ne le faisait pas automatiquement. On obtenait l'erreur suivante : *Models aren't loaded yet*

Ainsi nous avons rajouté la ligne **django.setup()** dans le fichier **webSite/urls.py**

### Test partie Django - IIS

Cliquer sur le site > Authentification > clic droit sur *Authentification anonyme* > Modifier > Identité du pool d'application

A ce stade le site fonctionne (normalement). Arreter le serveur puis relancer le et faire de même pour le site web. Aller ensuite sur localhost via IE. Si vous voyez une page de conexion alors parfait, sinon débugguer.

Source : http://www.helicontech.com/articles/running-django-on-windows-with-performance-tests/

### IIS - Active Directory

La suite est un test d'authentification**Kerberos** qui a été monté en local. Tou n'est donc pas à prendre (vous pouvez ignorer la création de l'AD par exemple)

Creer un AD en rajoutant un rôle au serveur. Creer une foret (HUGO.AD ici). Ajouter un serveur DNS

Ouvrir le centre d'administration de active director. HUGO > Domain Controllers > double clic sur le serveur > Délégation > Approuver délégation Kerberos

Cliquer sur le site > Authentification > désactiver authentification anonyme > activer authentification windows

Authentification Windows > Paramètres avancés > désactiver l'authentification du mode noyau

Authentification Windows > Fournisseurs > Supprimer tout et ne mettre que **Negotiate:Kerberos**

### 2nde magouille

A ce stade l'authentification devrait être opérationnelle. Cependant on veut que toutes les personnes se connectant en remote user aient accès à l'interface admin. Pour ce faire on va modifier le comportement par défaut de django :

Ouvrir le fichier C:/Python27/Lib/site-packages/django/contrib/auth/models.py

Modifier l'attribut is_superuser de PermissionMixin ligne 308 : changer *default=False* en *default=True*

Modifier l'attribut is_staff de AbstractUser ligne 400 : changer *default=False* en *default=True*

Ainsi les comptes créés automatiquement lors de la connexion via KERBEROS seront des comptes administrateur.

### export modèle et base de données

Ouvrir un cmd.exe dans le répertoire C:/www et executer :

	python manage.py migrate

## manage.py - l'outil d'administration

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

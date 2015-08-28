# Découverte de Django

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

## Developpement

### La structure des fichiers de Django

Commençons à la racine du projet (le premier répertoire webSite/).

Nous pouvons déjà voir le dossier *static* dans lequel sont stockés toutes les resources images, JS, CSS (cf manage.py ci-dessus).

Nous avons ensuite le dossier *webSite* qui porte le même nom que notre projet (le dossier racine). Ce dossier est en fait construit à la création du projet et contient les éléments de base d'un projet : le serveur Django integré (fichier *webSite/wsgi.py*), les paramètres de projet (fichier *webSite/settings.py*), le fichier de routage initial (*webSite/urls.py*). Nous reviendrons à ces deux derniers fichiers par la suite.

Nous avons également le fichier *manage.py* de la section précédente. Ce fichier n'est utile que pour l'administration du site (création de nouveaux modèles, ajout de fichiers static etc..).

Chacun des autres dossiers correspond à une *application* de KMAmossys. Cette application a un rôle bien précis ce qui permet de séparer les fonctionnalités du site Web. Par exemple l'application userManager gère les utilisateur, notamment leur connexion.

La structure d'une application Django respecte l'architecture Modèle/Vues/Controleurs. Prenons l'exemple de l'application *vuln* qui gère la base de connaissance vulnérabilités / recommandations :

#### Modèles - Models

Les modèles sont stockés dans le fichier *vuln/models.py*.

Un modèle représente une entité de la vie courante que l'on modélise par une classe. On peut définir le type des attributs de cette classe (ex : **models.IntegerField()** est un entier). Vous pouvez également mettre en place des relations entre les modèles (correspondance avec les clefs étrangères de sql). Vous pouvez par exemple voir dans l'objet **Vulnerabilite** qu'une Vulnérabilité est liée à plusieurs mots clefs grâce à ce champ :

	*mots_clefs = models.ManyToManyField(MotClef)*

#### Vues - Templates

Les Vues (ou templates en anglais) sont dans le répertoire *vuln/templates/vuln/*.

Une Vue est appelée par le controlleur (section suivante) avec tous les paramètres nécessaires, par exemple les Vulnerabilités (ou d'autres objets) à afficher. La Vue se charge alors d'afficher ces objets via du HTML.

Dans la Vue on peut aussi rencontrer un langage de templating. Ce langage permet de parcourir facilement les arguments que nous a envoyé le controlleur (section suivante), en faisant des boucles ou des conditions. Ce langage est destiné à être très facilement appris et est donc très proche de la langue courante mais également limité en fonctionnalité.

#### Controlleurs - Views

Les controlleurs (ou views en anglais) sont présents dans le fichier *vuln/models.py*.

Chaque fonction dans ce fichier correspond à une action. Une View va être appelé par l'utilisateur, elle parse sa requête et récupère les modèles que souhaite l'utilisateur. Une fois toutes les données néssaires à l'affichage la View envoie ces Models au Template pour qu'il puisse les afficher.

#### Routage

Le fichier *vuln/urls.py* définit quels controlleurs sont appelés en fonction de l'URL demandé par l'utilisateur. 

### Un exemple pour mieux comprendre

Pour que le rôle de chaque fichier soit plus clair, nous allons prendre un exemple. L'utilisateur demande l'URL /

Premièrement le projet charge ses paramètres depuis *webSite/settings.py* et cherche (entre autre) **ROOT_URLCONF = 'webSite.urls'**

Si on ouvre *webSite/urls.py* on voit que l'URL / est associée à une redirection vers *vuln:index*. 

On ouvre donc le fichier *vuln/urls.py* et on se rend compte que l'url *vuln:index* correspond à l'URL "/vulns/". En fait cette url (*vuln:index*) est un alias pour la véritable URL. Ceci permet de rendre le code plus maintenable et plus propre.

L'URL ne correspond d'ailleurs pas à "/vulns/" mais en réalité à "/vuln/vulns/" car on est dans le sous dossier *vuln*.

On constate (toujours dans *vuln/urls.py*) que l'URL en question possède en 2nd paramètre la chaîne *views.displayVuln*. Ce qui signifie que le controlleur appelé est la fonction *displayVuln* du fichier *vuln/views.py* (le fichier des controlleurs).

Pour résumer la première étape : **l'utilisateur demande "/" => webSite.urls le redirige vers /vuln/vulns/ (défini dans vuln.urls) qui appelle la fonction views.displayVuln**

On ouvre maintenant le fichier *vuln/views.py* et on s'intéresse à la fonction displayVuln(). Cette fonction récupère toutes les vulnérabilités et les mots clefs. Elle créé également un formulaire (le formulaire de recherche) puis envoie le tout au template *vuln/vulnerabilite_list.html*

On ouvre donc le template *vuln/templates/vuln/vulnerabilite_list.html* et on observe que d'autres templates sont inclus dans celui-ci. L'affichage se fait par couche au niveau du template car ceci est plus simple à manipuler. On remarque entre autre l'insertion du template *vuln/vulnerabilite_list_body.html*. Si on l'ouvre on peut (enfin) observer l'affichage du formulaire de reche. On peut également voir en bas du fichier l'affichage, via une boucle, des vulnérabilités récupérées préalablement dans la View.

### Ajout d'un champ à l'objet *Vulnerabilite*

Nous allons ajouter un champ 'nombre de consultations' à l'objet Vulnerabilite.

1. Ouvrir *vuln/models.py* et ajouter la ligne suivante sous la classe **Vulnerabilite** :

	nombre_de_consultations = models.PositiveIntegerField(default=0)

Ainsi nous avons ajouté un attribut obligatoire représentant un entier positif (pour le rendre optionnel, ajouter *blank*=True et *null*=True à la suite de *default*). Pour une liste des champs disponibles, regarder ici : https://docs.djangoproject.com/en/1.8/ref/models/fields/

2. Ouvrir un shell à la racine du projet (le premier dossier *webSite*) et lancer la commande :

	python manage.py makemigrations

Ceci prend en compte les modifications du modèle et stocke les modifications dans un cache qui est versionnable (par git ici).

3. Dans le même shell lancer la commande :

	python manage.py migrate

Ceci applique à la base de données les changements chargés grâce à la dernière commande.

4. Ouvrir *vuln/admin.py*. Ce fichier permet de personnaliser les champs disponibles dans l'interface administrateur. Vous pouvez voir une classe nommée VulnerabiliteAdmin, ajouter à la liste fieldsets l'entrée suivante :

	('Le nombre de fois que cette Vulnérabilité a été visitée', {'fields': ['nombre_de_consultations']})

ça y est vous pouvez relancer le serveur et votre nouveau champ est disponible ! Maintenant voyons où l'on peut s'en servir dans le code.

5. Ouvrir *vuln/templates/vuln/vulnerabilite_detail.html* et ajouter dans le *block body* la ligne suivante :

	Nombre de vues pour cette vulnérabilité : {{ vulnerabilite.nombre_de_consultations }}<br>

Et voilà ! Nous avons ajouté un champ en quelques clics. Bon développement.

### Générer une image de votre modèle de données

Installer les dépendances :

	sudo pip install pyparsing==1.5.7

	sudo pip install pydot

Lancer cette commande (en l'adaptant) :

	python manage.py graph_models -g -o <NOM>.png <Application à partir de laquelle générer l'image du modèle>

Par exemple :

	python manage.py graph_models -g -o diagramme.png vuln

### Création d'une nouvelle application

Pour vous aider a créer un nouvelle application (**monApp**) sur le site voici quelques conseils :    
1. Créer l'application avec `python manage.py startapp monApp`  
2. Mettre **monApp** dans la variable `INSTALLED_APPS` pour l'ajouter au site dans le fichier *webSite/setting.py*  
3. Ajouter une route de base du type `url(r'^maroute/', include('monApp.urls', namespace='monApp'))` dans *siteWeb/urls.py*  
4. Développer **monApp**  
  
* *Pour les* **modèles** *:*  
 * Vous pouvez établir des relations avec les utilisateurs en définissant une clé étrangère sur la classe `User`, importés comme ceci : `from django.contrib.auth.models import User`  
 * Pour établir cette relation penser à nommer la relation inverse c'est plus pratique, comme ceci : `Class Vuln(models.Model):` puis `user = models.ForeignKey(User, related_name='mes_vulns')`  
 * Après avoir créé vos modèles (inspirez vous de **vuln/models.py**) vous devez lancez ces commandes pour synchroniser la bdd :

	> python manage.py makemigrations # importe les changements dans un cache qui peut être versionné (par git entre autre)

	> python manage.py migrate        # prend en compte les changements précédemment importés et les insère dans la bdd (mysql ici) 
 
* *Pour les* **views** *(contrôleurs)* :  
  * Penser à ajouter le décorateur `@login_required` au dessus de vos actions, les utilisateurs déconnectés seront directement redirigés vers la page de connexion (pas encore développé avec le ldap d'Amossys)  
  * Ajouter une route vers votre action et nommez la dans **monApp/urls.py** (créez le fichier si besoin) comme ceci : `urlpatterns = [ url(r'^', views.index, name='index'),]`  
  
* *Pour les* **templates** *:*  
  * Copier le fichier *LTE/templates/LTE/starter.html*, et le renommer en **layout.html** dans **monApp/templates/monApp/**
  * Adapter et redéfinir tout les blocks du **layout.html** pour *monApp*  
  * Ce fichier **layout.html** sera la base de votre application, toute vos pages seront basées dessus  
  * Creer maintenant un **nouveau** template basé sur le fichier **LTE/templates/LTE/page.html**
  * Faire donc hériter le nouveau template de **monApp/templates/monApp/layout.html**  
  * Modifier le contenu de ce fichier pour qu'il corresponde à votre page   
  * *C'est bon !* Le templating en 3 couches (Base / Layout / Page) est terminé ! 
  * Si vous utilisez de l'**AJAX** passez par l'app ajax qui centralise ces requetes. Un **jeton csrf** est obligatoire même en ajax ! Infos [ici](https://docs.djangoproject.com/fr/1.7/ref/contrib/csrf/#csrf-ajax).   

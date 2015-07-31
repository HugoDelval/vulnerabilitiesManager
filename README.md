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

### Générer une image de votre modèle de données

sudo pip install pyparsing==1.5.7
sudo pip install pydot

python manage.py graph_models -g -o <NOM>.png <Application à partir de laquelle générer l'image du modèle>
python manage.py graph_models -g -o diagramme.png vuln


## Developpement



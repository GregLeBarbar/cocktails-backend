Backend python/django pour l'application cocktail
=================================================

Récupérer le code présent sur github
---------------------------------------

`git clone git@github.com:GregLeBarbar/cocktails-backend.git` 

<aside class="warning">
    Pour exécuter les commandes ci-dessous, vous devez être à la racine de votre projet.
</aside>

Créer un virtualenv python et installer les dépendances
-------------------------------------------------------

Pour créer un virtualenv python facilement, nous vous conseillons d'utiliser pyenv

[Doc installation pyenv](https://github.com/pyenv/pyenv#installation)

Créer le virtualenv coctails

`pyenv virtualenv 3.5.4 cocktails`

Activer le virtualenv coctails

`pyenv activate cocktails`

Installer les dépendances

`pip install -r requirements.txt`


Créer les migrations
--------------------

`python src/manage.py makemigrations apirest --settings=config.settings`

Créer les tables
----------------

`python src/manage.py migrate --settings=config.settings`

Lancer le serveur
-----------------

`python src/manage.py runserver --settings=config.settings`

Ajouter des éléments via un POST
-------------------------------

`http --json POST http://127.0.0.1:8000/api/v1/cocktails/ < mojito.json` 

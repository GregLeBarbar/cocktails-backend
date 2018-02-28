Backend python/django pour l'application cocktail
=================================================

## Installation

### Récupérer le code présent sur github


`git clone git@github.com:GregLeBarbar/cocktails-backend.git` 

<aside class="warning">
    Pour exécuter les commandes ci-dessous, vous devez être à la racine du projet.
</aside>

### Créer un virtualenv python et installer les dépendances

Pour créer un virtualenv python facilement, nous vous conseillons d'utiliser pyenv

[Doc installation pyenv](https://github.com/pyenv/pyenv#installation)

Créer le virtualenv cocktails

`pyenv virtualenv 3.5.4 cocktails`

Activer le virtualenv cocktails

`pyenv activate cocktails`

Installer les dépendances

`pip install -r requirements.txt`


### Lancer le serveur

`python src/manage.py runserver --settings=config.settings`

### Accéder à l'api REST
`http://127.0.0.1:8000/api/v1/cocktails/`


### Ajouter des nouveaux cocktails

Exemple:

`http --json POST http://127.0.0.1:8000/api/v1/cocktails/ < mojito.json` 

## CORS (Cross-Origin Resource Sharing)

Le package django-cors-headers ajoute les headers CORS aux réponses HTTP



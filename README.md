# Contact Manager Postgres

Une application Python en ligne de commande pour gérer une liste de contacts stockée dans une base PostgreSQL.

## Fonctionnalités

- Ajouter un contact
- Afficher la liste des contacts
- Supprimer un contact

## Prérequis

- Python 3.10+
- [Docker](https://www.docker.com/) (pour utiliser un conteneur PostgreSQL)

## Installation

1. Clone ce dépôt :
   ```sh
   git clone https://github.com/ton-utilisateur/contact_manager_postgres.git
   cd contact_manager_postgres
   ```

2. Installe les dépendances :
   ```sh
   pip install -r requirements.txt
   ```

3. Configure la base de données :
   - Créer et modifier un fichier `.env` avec les variables suivantes:
    ```sh
     DB_NAME=...
     DB_USER=...
     DB_PASSWORD=...
     DB_HOST=...
     DB_PORT=...

     POSTGRES_DB=...
     POSTGRES_USER=...
     POSTGRES_PASSWORD=...
     ```
     NB: Remplacer les "..." par vos identifiants que vous voulez utiliser

   - Tu peux lancer PostgreSQL avec Docker :
     ```sh
     docker-compose up -d
     ```

## Utilisation

Lance l'application :
```sh
python src/main.py
```

Suis les instructions dans le terminal pour gérer tes contacts.

## Auteur

Komlan Erwin
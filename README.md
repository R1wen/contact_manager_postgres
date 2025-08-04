# Contact Manager Postgres

Une application Python en ligne de commande pour gérer une liste de contacts stockée dans une base PostgreSQL.

## Fonctionnalités

- Ajouter un contact
- Afficher la liste des contacts
- Supprimer un contact
- Modifier un contact

## Prérequis

- Python 3.10+
- [Docker](https://www.docker.com/) (pour utiliser un conteneur PostgreSQL)

## Installation

1. Clone ce dépôt :
   ```sh
   git clone https://github.com/R1wen/contact_manager_postgres
   cd contact_manager_postgres
   ```

2. Crée et active un environnement virtuel :
   ```sh
   python -m venv venv
   # Sous Windows :
   venv\Scripts\activate
   # Sous macOS/Linux :
   source venv/bin/activate
   ```

3. Installe les dépendances :
   ```sh
   pip install -r requirements.txt
   ```

4. Configure la base de données :
   - Crée et modifie un fichier `.env` avec les variables suivantes :
     ```sh
     DB_NAME=...
     DB_USER=...
     DB_PASSWORD=...
     DB_HOST=...
     DB_PORT=...
     ```
     NB : Remplace les "..." par tes identifiants.

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

Komlan Erwin OKE
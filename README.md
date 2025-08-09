# Contact Manager Postgres

Une application Python (Flask) et frontend web pour gérer une liste de contacts stockée dans une base PostgreSQL.

## Fonctionnalités

- Ajouter un contact
- Afficher la liste des contacts
- Supprimer un contact
- Modifier un contact

## Prérequis

- [Docker](https://www.docker.com/)

## Installation et lancement

1. Clone ce dépôt :
   ```sh
   git clone https://github.com/R1wen/contact_manager_postgres
   cd contact_manager_postgres
   code .
   ```

2. Configure la base de données :
   - Crée et modifie un fichier `.env` à la racine avec les variables suivantes :
     ```sh
     DB_NAME=...
     DB_USER=...
     DB_PASSWORD=...
     DB_HOST=postgres
     DB_PORT=...
     ```
     NB : Remplace les "..." par les identifiants souhaités.

3. Lance tous les services (PostgreSQL, API Flask, frontend) :
   ```sh
   docker-compose up --build -d
   ```

4. Accède à l'application :
   - Frontend : [http://localhost:8080](http://localhost:8080)
   - API : [http://localhost:5000](http://localhost:5000)

## Utilisation

- Utilise l'interface web pour gérer tes contacts.
- Les données sont stockées

## Auteur

Komlan Erwin OKE
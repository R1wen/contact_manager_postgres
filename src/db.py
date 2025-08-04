import psycopg2

from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connexion à PostgreSQL réussie")
        return conn
    except psycopg2.OperationalError as e:
        print("Erreur de connexion à PostgreSQL: ")
        print(e)
        return None

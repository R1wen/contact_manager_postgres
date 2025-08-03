from db import get_connection


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS contacts (
                            id SERIAL PRIMARY KEY,
                            nom VARCHAR(100),
                            prenom VARCHAR(100),
                            telephone VARCHAR(20)
                        )
                        """)
            conn.commit()


def add_contact(nom: str, prenom: str, telephone: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                (
                    "INSERT INTO contacts (nom, prenom, telephone) "
                    "VALUES (%s, %s, %s)"
                ),
                (nom, prenom, telephone)
            )
            conn.commit()


def list_contact():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM contacts"
            )
            rows = cur.fetchall()
            for row in rows:
                id, nom, prenom, telephone = row
                print(f"{id}. {nom} {prenom} | tel: {telephone}")
        conn.commit()

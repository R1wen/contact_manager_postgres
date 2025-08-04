from db import get_connection


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                            CREATE TABLE IF NOT EXISTS contacts (
                                id SERIAL PRIMARY KEY,
                                nom VARCHAR(100),
                                prenom VARCHAR(100),
                                telephone VARCHAR(20)
                            )
                            """)
                conn.commit()
            except Exception as e:
                print(
                    "Une erreur est survenue lors de la création de la table:", e
                )


def add_contact(nom: str, prenom: str, telephone: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    (
                        "INSERT INTO contacts (nom, prenom, telephone) "
                        "VALUES (%s, %s, %s)"
                    ),
                    (nom, prenom, telephone)
                )
                conn.commit()
            except Exception as e:
                print("Erreur lors de l'ajout du contact: ", e)


def list_contact():
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "SELECT * FROM contacts"
                )
                rows = cur.fetchall()
                for index, row in enumerate(rows):
                    id, nom, prenom, telephone = row
                    print(
                        (
                            f"{index + 1}. {nom} {prenom} | tel: {telephone}, "
                            f"(ID réel: {id})"
                        )
                    )
                conn.commit()
            except Exception as e:
                print("Erreur lors de l'affichage: ", e)


def delete_contact(nom: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM contacts where nom = %s", (nom,)
                )
                conn.commit()
            except Exception as e:
                print("Erreur lors de la suppression: ", e)


def update_contact(id: int, nom: str, prenom: str, telephone: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    UPDATE contacts
                    SET nom = %s, prenom = %s, telephone = %s
                    WHERE id = %s
                    """, (nom, prenom, telephone, id)
                )
                conn.commit()
            except Exception as e:
                print("Erreur lors de la modification: ", e)

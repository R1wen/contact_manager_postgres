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
                contacts = []
                for row in rows:
                    id, nom, prenom, telephone = row
                    contacts.append({
                        "id": id,
                        "nom": nom,
                        "prenom": prenom,
                        "telephone": telephone
                    })
                conn.commit()
                return contacts
            except Exception as e:
                print("Erreur lors de l'affichage: ", e)
                return []


def find_contact(id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "SELECT * FROM contacts WHERE id=%s", (id,)
                )
                row = cur.fetchone()
                if row:
                    id, nom, prenom, telephone = row
                    contact = {
                        "id": id,
                        "nom": nom,
                        "prenom": prenom,
                        "telephone": telephone
                    }
                conn.commit()
                return contact
            except Exception as e:
                print("Erreur lors de l'affichage: ", e)
                return None


def delete_contact(id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM contacts where id = %s", (id,)
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

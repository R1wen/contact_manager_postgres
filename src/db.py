import psycopg2

from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


def get_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn


# if __name__ == "__main__":
#     try:
#         conn = get_connection()
#         print("Succes")
#         conn.close()
#     except Exception as e:
#         print("Echec : ", e)

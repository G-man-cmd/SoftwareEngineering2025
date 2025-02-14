import psycopg2

def get_connection():
    try:
        return psycopg2.connect(
            database="photon",
            user="postgres",
            password="student",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False
conn = get_connection()
cursor = conn.cursor()
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered an error.")
    sys.exit()

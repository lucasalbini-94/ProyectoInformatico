import mysql.connector
<<<<<<< HEAD

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="portfolio"  # 👈 Cambiá por el nombre real
    )
=======
import os

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df

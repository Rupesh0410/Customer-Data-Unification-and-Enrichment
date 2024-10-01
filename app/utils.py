# app/utils.py
import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE

def setup_database():
    connection = mysql.connector.connect(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE};")
    cursor.execute(f"USE {MYSQL_DATABASE};")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INT PRIMARY KEY,
            name VARCHAR(255),
            job_title VARCHAR(255)
        );
    """)
    connection.close()

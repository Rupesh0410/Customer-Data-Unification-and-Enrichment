# app/load.py
import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE
import logging

logging.basicConfig(level=logging.INFO)

def load_data(data=None, fetch=False):
    connection = mysql.connector.connect(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        database=MYSQL_DATABASE
    )
    cursor = connection.cursor()

    if fetch:
        cursor.execute("SELECT * FROM customers")
        return cursor.fetchall()

    # Assuming data is a Pandas DataFrame
    for _, row in data.iterrows():
        cursor.execute("""
            INSERT INTO customers (customer_id, name, job_title)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            name=VALUES(name),
            job_title=VALUES(job_title);
        """, (row['customer_id'], row['name'], row['job_title']))

    connection.commit()
    connection.close()
    logging.info("Data loaded into MySQL successfully.")

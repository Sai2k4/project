# databaseconnection.py
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SaiRam@090904",
        database="pypro"
    )
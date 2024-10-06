# app/__init__.py
from flask import Flask
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
import mysql.connector

app = Flask(__name__)

# Database connection function
def connect_to_db():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection

from app import routes

from flask import Flask
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="hjemmeside"
    )
cursor = mydb.cursor()

mysql = MySQL(app)

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
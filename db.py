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
print("hej")
mysql = MySQL(app)

def create_post(name,post):
    cursor.execute("INSERT INTO omos (name,post) VALUES (%s,%s)",(name,post))
    mydb.commit()

def get_posts():
    cursor.execute("SELECT * FROM omos")
    posts = cursor.fetchall()
    return posts

def user_login(username, password):
    cursor.execute("SELECT * FROM bruger WHERE username LIKE (%s) AND passwd LIKE (%s)",(username, password))
    bruger = cursor.fetchone()
    print (bruger)
    return bruger


def create_user(username, password):
    cursor.execute("INSERT INTO bruger (username, passwd) VALUES (%s,%s)",(username, password))
    mydb.commit()



#cursor.execute("INSERT INTO bruger (username, passwd) VALUES (%s, %s)",("diller","pepepe"))


mydb.commit()
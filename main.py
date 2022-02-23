from flask import Flask, render_template,request,redirect,session
from db import cursor, mydb, create_user,user_login

app = Flask(__name__)

app.config["SECRET_KEY"]="1234"

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/login',methods=['POST',"GET"])
def login():
    if request.method == 'POST':
        user=request.form["brugernavn"]
        passwd = request.form["pass"]
        bruger = user_login(user,passwd)
        print(bruger)
        if bruger:
            session["loggedin"] = True
            session["id"]=bruger[0]
            session["username"] = bruger[1]
            return redirect("/login")
        else:
            return "not logged in"
    return render_template('login.html',username=session["username"])



@app.route('/register', methods=['POST',"GET"])
def register():
    if request.method == 'POST':
        username = request.form["brugernavn"]
        password = request.form["pass"]
        create_user(username,password)
    else:
        pass
    return render_template('register.html')



if __name__ == '__main__':
    app.run()
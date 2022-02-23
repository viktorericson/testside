from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login',methods=['POST',"GET"])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
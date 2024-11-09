from flask import Flask, render_template
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
import re


app = Flask(__name__, template_folder="api/html")

@app.route("/home.html")
def index():
    return render_template("home.html")
    
def dbConnect():
    connect = psycopg2.connect(host= process.env.POSTGRES_HOST,
                            database= process.env.POSTGRES_DATABASE,
                            user= process.env.POSTGRES_USER,
                            password= process.env.POSTGRES_PASSWORD)
    return conn

@app.route("/aboutUs.html")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/calendar.html")
def calendar():
    return render_template("calendar.html")

@app.route("/howItWorks.html")
def howItWorks():
    return render_template("howItWorks.html")

@app.route("/login.html", methods=["GET", "POST"])
def page():
    return render_template("login.html")
def login():
    
    conn = dbConnect()
    cur = conn.cursor()
    
def register():
    
    conn = dbConnect()
    cur = conn.cursor()
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conf = request.form.get("conf")

        if not username:
            return "no username"
        elif cur.execute("SELECT username FROM users WHERE username = ?", username):
            return "username already belongs to someone else"
        elif not password:
            return "no password"
        elif len(password) < 8:
            return "password must be 8 characters or longer"
        elif re.search('[0-9]',password):
            return "password must contain a number"
        elif re.search('[A-Z]',password):
            return "password must contain one uppercase letter"
        elif re.search('[!@#$%^&*()<>?:;]', password):
            return "password must contain one special character"
        elif not conf:
            return "must provide password confirmation"
        elif (password != conf)
            return "password and confirmation do not match"

    curr.execute("INSERT INTO users (username, hash) VALUES ('?', '?')", username, generate_password_hash(password))

    return render_template("calendar.html")


@app.route("/")
def fallback():
    return render_template("home.html")


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("error.html"), 404

@app.errorhandler(500)
def pageNotFound(error):
    return render_template("internal.html"), 500


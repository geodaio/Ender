from flask import Flask, render_template

app = Flask(__name__, template_folder="api/html")

@app.route("/home.html")
def index():
    return render_template("home.html")

@app.route("/aboutUs.html")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/calendar.html")
def calendar():
    return render_template("calendar.html")

@app.route("/howItWorks.html")
def howItWorks():
    return render_template("howItWorks.html")

@app.route("/")
def fallback():
    return render_template("home.html")
    
@app.route("/*")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run()
    

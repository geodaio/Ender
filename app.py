from flask import Flask, render_template

app = Flask(__name__, template_folder="api/html")

@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
    

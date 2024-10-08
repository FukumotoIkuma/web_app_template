from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/volume")
def volume():
    return render_template("volume.html")

if __name__ == "__main__":
    app.run(debug=True)

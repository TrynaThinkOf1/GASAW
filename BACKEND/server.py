from flask import Flask, render_template
from os import path

app = Flask(__name__, template_folder = path.join("../FRONTEND", "templates"))

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
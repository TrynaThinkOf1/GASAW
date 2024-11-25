from flask import Flask, render_template, jsonify, request, redirect
from os import path

import _mailman

type_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7}

app = Flask(__name__, template_folder="../FRONTEND/templates", static_folder="../FRONTEND/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_data", methods=["GET"])
def get_data():
    type = request.args.get("type")
    if type in type_map:
        return jsonify(_handler.get_data(type_map[type]))
    else:
        return jsonify({"error": "Invalid type"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
from flask import Flask, render_template, send_file, request, redirect
from os import path

import _mailman
from BACKEND import _seismic

type_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7}

app = Flask(__name__, template_folder="../FRONTEND/templates", static_folder="../FRONTEND/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/seismic_plot", methods=['GET'])
def seismic_plot():
    plot_img = _mailman.getSeismicPlot()
    return send_file(plot_img, mimetype='image/png')

@app.route("/seismic")
def seismic():
    return render_template("seismic.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
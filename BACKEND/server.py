from flask import Flask, render_template, send_file, request, jsonify

import _mailman  # effective middle-man

app = Flask(__name__, template_folder="../FRONTEND/templates", static_folder="../FRONTEND/static")

eventData = []

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


@app.route("/seismic_event_data")
def seismic_data():
    ev_data = _mailman.getSeismicData()  # Fetch the updated seismic data
    return jsonify(ev_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
from flask import Flask, render_template, send_file, request, jsonify, redirect

import _mailman  # effective middle-man

app = Flask(__name__, template_folder="../FRONTEND/templates", static_folder="../FRONTEND/static")

eventData = []
plot_img = None

@app.route("/")
def index():
    return render_template("index.html")

############################
#       SEISMIC PAGES      #
############################
@app.route("/seismic")
def seismic():
    return render_template("seismic.html")

@app.route("/get_seismic_plot", methods=['GET'])
def seismic_plot():
    global plot_img

    try:
        min_magnitude = float(request.args.get('min_magnitude'))
        measure_period = int(request.args.get('measure_period'))

        plot_img = _mailman.getSeismicPlot(min_magnitude, measure_period)
        return redirect("/seismic", code=302)
    except Exception as e:
        return str(e)

@app.route("/view_seismic_plot")
def view():
    return send_file(plot_img, mimetype='image/png')

@app.route("/seismic_event_data")
def seismic_data():
    ev_data = _mailman.getSeismicData()  # Fetch the updated seismic data
    return jsonify(ev_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
import flask
import pandas as pd

app = flask.Flask(__name__)

stations = pd.read_csv("data/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return flask.render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt" # zfill nam naredi 000066
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"]) # Preskočimo prvih 20 vrstic ker je se vsi fili začne na 21 vrstic
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze() / 10

    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)

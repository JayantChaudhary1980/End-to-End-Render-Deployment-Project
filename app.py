import pickle

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

with open("model/house_price_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["MedInc"]),
        float(request.form["HouseAge"]),
        float(request.form["AveRooms"]),
        float(request.form["AveBedrms"]),
        float(request.form["Population"]),
        float(request.form["AveOccup"]),
        float(request.form["Latitude"]),
        float(request.form["Longitude"]),
    ]

    df = pd.DataFrame([features], columns=[
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude",
    ])

    prediction = model.predict(df)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 3)
    )


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load data
data = pd.read_csv("fabrics.csv")

# Create sustainability score (target)
data["SustainabilityScore"] = (
    100
    - data["Carbon"] * 10
    - data["Water"] / 100
    + data["Biodegradable"] * 15
)

# Train ML model
X = data[["Carbon", "Water", "Biodegradable", "Cost", "Durability"]]
y = data["SustainabilityScore"]

model = LinearRegression()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        budget = int(request.form["budget"])
        durability = int(request.form["durability"])
        climate = request.form["climate"]

        # Filter based on user input
        filtered = data[
            (data["Cost"] <= budget) &
            (data["Durability"] >= durability) &
            (data["Climate"] == climate)
        ]

        if not filtered.empty:
            features = filtered[["Carbon", "Water", "Biodegradable", "Cost", "Durability"]]
            filtered["PredictedScore"] = model.predict(features)
            result = filtered.sort_values(by="PredictedScore", ascending=False).iloc[0]

    return render_template("index.html", fabric=result)

if __name__ == "__main__":
    app.run(debug=True)

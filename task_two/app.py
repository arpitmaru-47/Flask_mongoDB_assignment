from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://appi:appi123@cluster0.galxbbc.mongodb.net/?appName=Cluster0"
)

db = client["studentdb"]

collection = db["students"]


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    try:

        name = request.form["name"]
        age = request.form["age"]
        city = request.form["city"]

        data = {
            "name": name,
            "age": age,
            "city": city
        }

        collection.insert_one(data)

        return render_template("success.html")

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


if __name__ == "__main__":

    app.run(debug=True)
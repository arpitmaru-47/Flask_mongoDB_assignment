from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api")
def api():

    file = open("data.json")

    data = json.load(file)

    return jsonify(data)

if __name__ == "__main__":

    app.run(debug=True)
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["devops_config_db"]
collection = db["configurations"]


@app.route("/config", methods=["GET"])
def get_config():
    data = collection.find_one(sort=[("_id", -1)])

    if data:
        data.pop("_id")  # MongoDB internal field remove
        return jsonify(data)

    return jsonify({"error": "Any configuration data not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

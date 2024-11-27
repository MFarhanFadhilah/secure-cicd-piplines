from flask import Flask, Blueprint, jsonify, request

app = Flask(__name__)

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"message": "Hello, World!"})

@main.route("/data", methods=["POST"])
def process_data():
    data = request.get_json()
    if not isinstance(data, dict):  # data validation
        return jsonify({"error": "Invalid data format"}), 400
    return jsonify({"processed": True, "data": data})

app.register_blueprint(main)

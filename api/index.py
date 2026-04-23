import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CLOUD_NAME    = os.getenv("CLOUDINARY_CLOUD_NAME")
UPLOAD_PRESET = os.getenv("CLOUDINARY_UPLOAD_PRESET")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    response = requests.post(
        f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/image/upload",
        data={"upload_preset": UPLOAD_PRESET},
        files={"file": (file.filename, file.stream, file.mimetype)},
    )

    return jsonify(response.json()), response.status_code

from app import app
from flask import jsonify

status={
    'humidity': 0
}

@app.route('/status' ,methods=["GET"])
def get_status():
    return jsonify(status)
from app import app
from flask import jsonify
from app.api.db import dbapi

@app.route('/status' ,methods=["GET"])
def get_status():
    status = dbapi.get_current_status()
    return jsonify(status)

@app.route('/status' ,methods=["POST"])
def update_status():
    status = dbapi.update_status()
    return status

@app.route('/history', methods=["GET"])
def get_history():
    hist = dbapi.get_all_history()
    return jsonify(hist)

@app.route("/history", methods=["POST"])
def save_history():
    hist = dbapi.save_history_to_db()
    return hist
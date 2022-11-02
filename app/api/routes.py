from app import app
from flask import jsonify
from app.api.db import dbapi

@app.route('/status' ,methods=["GET"])
def get_status():
    status = dbapi.get_current_status()
    return jsonify(status)
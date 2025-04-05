from flask import Blueprint, jsonify

example_bp = Blueprint('example', __name__)

@example_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "online", "message": "Command Control System is operational."})
from ..utils.offline_mode import is_offline, toggle_offline

@example_bp.route('/status', methods=['GET'])
def status():
    mode = "offline" if is_offline() else "online"
    return jsonify({"mode": mode})

@example_bp.route('/toggle', methods=['POST'])
def toggle():
    state = toggle_offline()
    return jsonify({"offline_mode": state})

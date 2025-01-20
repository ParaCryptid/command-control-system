
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import geojson
from transformers import pipeline

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize AI models (e.g., sentiment analysis for commands)
command_analyzer = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return jsonify({
        "message": "Command and Control System repository is fully functional.",
        "features": [
            "AI-Powered Command Analysis",
            "Real-Time Command Updates",
            "Secure Collaboration",
            "Geospatial Monitoring"
        ]
    })

@app.route('/analyze_command', methods=['POST'])
def analyze_command():
    data = request.json.get("command", "")
    if not data:
        return jsonify({"error": "No command provided"}), 400
    analysis = command_analyzer(data)
    return jsonify({"analysis": analysis})

@app.route('/geospatial_event', methods=['POST'])
def report_geospatial_event():
    data = request.json
    if not data or "latitude" not in data or "longitude" not in data:
        return jsonify({"error": "Invalid geospatial data"}), 400

    event = geojson.Feature(
        geometry=geojson.Point((data["longitude"], data["latitude"])),
        properties={"event_type": data.get("event_type", "Unknown")}
    )
    socketio.emit("geospatial_event", {"event": geojson.dumps(event)})
    return jsonify({"message": "Geospatial event reported successfully", "event": event})

@socketio.on('connect')
def handle_connect():
    emit("message", {"message": "Real-time command updates connection established"})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)

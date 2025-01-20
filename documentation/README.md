
# Command Control System

## Overview
The Command Control System has been enhanced with new features to improve functionality and enable secure collaboration.

### New Features
1. **AI-Powered Command Analysis**
    - Endpoint: `/analyze_command`
    - Method: `POST`
    - Description: Analyzes the sentiment of provided commands for prioritization.
    - Example Request:
      ```json
      {
          "command": "Deploy resources to location X immediately."
      }
      ```
    - Example Response:
      ```json
      {
          "analysis": [{"label": "POSITIVE", "score": 0.98}]
      }
      ```

2. **Real-Time Command Updates**
    - Enables real-time command communication and updates using Flask-SocketIO.

3. **Geospatial Monitoring**
    - Endpoint: `/geospatial_event`
    - Method: `POST`
    - Description: Reports and visualizes geospatial events.
    - Example Request:
      ```json
      {
          "latitude": 34.05,
          "longitude": -118.25,
          "event_type": "Deployment"
      }
      ```
    - Example Response:
      ```json
      {
          "message": "Geospatial event reported successfully",
          "event": {...}
      }
      ```

### Getting Started
1. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the application:
    ```bash
    python app.py
    ```

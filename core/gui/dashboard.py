import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

dashboard_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Tactical Command Dashboard</title>
    <style>
        body { background-color: #0a0a0a; color: #00ffcc; font-family: monospace; padding: 20px; }
        h1 { color: #00ffff; }
        button { background: #222; color: #0f0; border: 1px solid #0f0; padding: 10px; margin: 5px; }
    </style>
</head>
<body>
    <h1>Tactical Dashboard - Role: {{ role }}</h1>
    <form method="post">
        <input type="hidden" name="role" value="{{ role }}">
        {% if role == 'admin' %}
            <button name="action" value="backup">Run GPG Backup</button>
            <button name="action" value="heal">Trigger Self-Heal</button>
            <button name="action" value="recon">Run AI Recon</button>
        {% endif %}
        <button name="action" value="cam">Launch Surveillance</button>
        <button name="action" value="airgap_on">Airgap ON</button>
        <button name="action" value="airgap_off">Airgap OFF</button>
    </form>
    <pre>{{ output }}</pre>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def dashboard():
    role = request.form.get("role", "agent")
    output = ""

    if request.method == "POST":
        action = request.form.get("action")
        if action == "backup":
            output = os.popen("python3 core/backup/backup_manager.py").read()
        elif action == "heal":
            output = os.popen("python3 core/watchdogs/self_heal.py &").read()
        elif action == "recon":
            output = os.popen("python3 core/recon/ai_recon.py").read()
        elif action == "cam":
            os.system("python3 core/surveillance/cam_control.py &")
            output = "Surveillance launched."
        elif action == "airgap_on":
            os.system("bash offline/airgap_toggle.sh on")
            output = "Airgap activated."
        elif action == "airgap_off":
            os.system("bash offline/airgap_toggle.sh off")
            output = "Airgap deactivated."

    return render_template_string(dashboard_template, role=role, output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
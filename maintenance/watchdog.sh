#!/bin/bash
# Simple watchdog to ensure app stays online

if ! pgrep -f "run.py" > /dev/null
then
    echo "[Watchdog] App is down. Restarting..."
    cd "$(dirname "$0")"/..
    nohup python3 run.py > watchdog.log 2>&1 &
else
    echo "[Watchdog] App is running."
fi
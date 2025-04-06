
import cv2
import os
import time
import subprocess
from datetime import datetime

OUTPUT_DIR = "/classified"
GPG_RECIPIENT = "System Unlock <tactical@localhost>"

def encrypt_file(file_path):
    encrypted_path = file_path + ".gpg"
    try:
        subprocess.run([
            "gpg", "--yes", "--output", encrypted_path,
            "--encrypt", "--recipient", GPG_RECIPIENT, file_path
        ], check=True)
        os.remove(file_path)
        print(f"[{datetime.now()}] Encrypted: {file_path}")
    except subprocess.CalledProcessError:
        print(f"[{datetime.now()}] Failed to encrypt: {file_path}")

def motion_detector():
    cam = cv2.VideoCapture(0)
    time.sleep(2)
    first_frame = None

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if first_frame is None:
            first_frame = gray
            continue

        delta = cv2.absdiff(first_frame, gray)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        if cv2.countNonZero(thresh) > 5000:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{OUTPUT_DIR}/capture_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"[{datetime.now()}] Motion detected, image saved.")
            encrypt_file(filename)
            time.sleep(5)  # pause to avoid repeated triggering

    cam.release()

if __name__ == "__main__":
    motion_detector()

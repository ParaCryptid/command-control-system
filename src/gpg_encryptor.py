
import os
import subprocess
from datetime import datetime

# Paths
TARGET_DIRS = ["/classified", "/dropzone"]
GPG_RECIPIENT = "System Unlock <tactical@localhost>"

def encrypt_files():
    for folder in TARGET_DIRS:
        abs_folder = os.path.abspath(folder)
        for filename in os.listdir(abs_folder):
            full_path = os.path.join(abs_folder, filename)
            if os.path.isfile(full_path) and not filename.endswith(".gpg"):
                encrypted_path = full_path + ".gpg"
                try:
                    subprocess.run([
                        "gpg", "--yes", "--output", encrypted_path,
                        "--encrypt", "--recipient", GPG_RECIPIENT, full_path
                    ], check=True)
                    os.remove(full_path)
                    print(f"[{datetime.now()}] Encrypted: {filename}")
                except subprocess.CalledProcessError:
                    print(f"[{datetime.now()}] Failed to encrypt: {filename}")

if __name__ == "__main__":
    encrypt_files()

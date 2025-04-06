import os
import subprocess
from datetime import datetime

def run_backup():
    source_dir = '/classified'
    dest_dir = '/mnt/usb_encrypted'
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    archive_name = f"{dest_dir}/classified_backup_{timestamp}.tar.gpg"

    os.makedirs(dest_dir, exist_ok=True)
    subprocess.run([
        'tar', '-czf', '-', source_dir
    ], stdout=subprocess.PIPE)
    subprocess.run([
        'gpg', '--encrypt', '--recipient', 'tactical@localhost', '--output', archive_name
    ])

if __name__ == "__main__":
    run_backup()
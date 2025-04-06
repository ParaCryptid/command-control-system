import subprocess
import time

SERVICES = ['recon', 'dashboard', 'surveillance']

def check_and_restart(service):
    status = subprocess.run(['pgrep', '-f', service], capture_output=True)
    if status.returncode != 0:
        print(f"[!] {service} is down. Restarting...")
        subprocess.Popen([f'/usr/local/bin/{service}_start.sh'])

def main():
    while True:
        for service in SERVICES:
            check_and_restart(service)
        time.sleep(60)

if __name__ == "__main__":
    main()
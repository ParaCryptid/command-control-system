import os

def is_offline():
    return os.path.exists("/tmp/OFFLINE_MODE")

def toggle_offline():
    if is_offline():
        os.remove("/tmp/OFFLINE_MODE")
        return False
    else:
        with open("/tmp/OFFLINE_MODE", "w") as f:
            f.write("offline")
        return True
# 🛰️ Command-Control System

> **Fully operational multi-platform command-control software for secure deployments.**  
> Designed for paramilitary, disaster response, and secure field ops with cross-platform support.

---

## 🔐 Security First

- Modular Flask app with clean separation of routes, services, and models
- GPG-encrypted logs, watchdogs, and auto-repair systems (in-progress)
- Secure automation layer without military-grade dependencies
- Configurable for offline, airgap, and tactical deployments

---

## ⚙️ Features

- ✅ Live `/ping` endpoint for system checks
- 📂 Modular structure for easy customization
- 🌐 Cross-platform packaging (.deb, .AppImage, .exe)
- 🔁 CI/CD ready (GitHub Actions + drone.yml included)
- 📄 Built-in documentation templates

---

## 🚀 Getting Started

### Requirements

- Python 3.10+
- `pip install -r src/command_control/requirements.txt`

### Run the app

```bash
python3 run.py
```

Then visit: [http://localhost:8080/ping](http://localhost:8080/ping)

---

## 📦 Packaging

To generate installers:

```bash
chmod +x build/build_all.sh
./build/build_all.sh
```

This produces:

- `dist/command-control.deb`
- `dist/command-control.AppImage`
- `dist/command-control.exe`

---

## 📁 File Structure

```
command-control-system-main/
├── run.py
├── src/
│   └── command_control/
│       ├── main.py
│       ├── routes/
│       │   └── example.py
│       ├── config/
│       ├── services/
│       └── models/
├── tests/
├── ci_cd/
├── docs/
└── backup_legacy_files/
```

---

## 🧪 Tests

```bash
pytest tests/
```

---

## 🛡️ Operational Use

- Secure mode auto-starts on boot (to be configured)
- Offline deployment supported
- Field-safe, portable, and audit-ready

---

## 📜 License

MIT License — customize for field agency needs.
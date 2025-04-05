# 🧑‍💻 User Guide

## Starting the App

```bash
python3 run.py
```

Visit [http://localhost:8080/ping](http://localhost:8080/ping)

## Status Mode

- GET `/status` to check if offline mode is enabled
- POST `/toggle` to toggle offline mode

## Backup

```bash
./maintenance/gpg_backup.sh
```
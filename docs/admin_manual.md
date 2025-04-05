# 🔧 Admin Manual

## Watchdog Setup

Use `cron` to keep app online:

```cron
* * * * * /path/to/watchdog.sh
```

## Secure Backup

Encrypt the current app state:

```bash
./maintenance/gpg_backup.sh
```

## Build for Distribution

```bash
./build/build_all.sh
```
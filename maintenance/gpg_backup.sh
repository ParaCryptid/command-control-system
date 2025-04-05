#!/bin/bash
# GPG encrypt the logs and configs for secure backup

timestamp=$(date +'%Y%m%d_%H%M%S')
output="backups/backup_$timestamp.tar.gz.gpg"
mkdir -p backups

tar czf - src/command_control/ > temp.tar.gz
gpg --yes --batch --recipient "robshubert96@gmail.com" --encrypt temp.tar.gz
mv temp.tar.gz.gpg "$output"
rm temp.tar.gz

echo "[Backup] Encrypted backup created at: $output"
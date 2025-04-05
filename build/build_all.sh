#!/bin/bash
set -e

echo "[*] Starting universal build..."

# Clean previous builds
rm -rf dist
mkdir -p dist

# 1. Build .deb package (Ubuntu/Debian)
echo "[*] Building .deb package..."
mkdir -p build/deb_package/usr/local/bin
cp run.py build/deb_package/usr/local/bin/command-control
fpm -s dir -t deb -n command-control -v 1.0.0 -C build/deb_package -p dist/command-control.deb

# 2. Build AppImage (Portable Linux)
echo "[*] Building .AppImage..."
pyinstaller --onefile --name command-control src/command_control/main.py
mv dist/command-control dist/command-control.AppImage

# 3. Build Windows executable
echo "[*] Building .exe for Windows..."
pyinstaller --onefile --name command-control.exe src/command_control/main.py
mv dist/command-control.exe dist/command-control.exe

echo "[✔] Build complete. Files in ./dist:"
ls -lh dist/
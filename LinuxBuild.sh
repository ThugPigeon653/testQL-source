#!/bin/bash
chmod +x dist/set-path.sh
pip install pyinstaller
pyinstaller --onefile testQL.py
pyinstaller --onefile --add-data "config.json;." testQL.py
mv set-path.bat dist/set-path.sh
./dist/set-path.sh
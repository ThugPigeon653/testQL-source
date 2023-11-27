cd %~dp0
pip install pyinstaller
pyinstaller --onefile testQL.py
pyinstaller --onefile --add-data "config.json;." testQL.py
move set-path.bat dist/set-path.bat
call dist/set-path.bat
pause
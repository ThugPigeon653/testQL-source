set "TOOL_DIR=%~dp0"
cd /d "%TOOL_DIR%"
echo %cd%
setx PATH "%cd%;%PATH%" /m

pause
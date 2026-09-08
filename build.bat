@echo off
setlocal
cd /d "%~dp0"
python -m PyInstaller --noconfirm --clean EnglishCourseAI.spec
if errorlevel 1 exit /b %errorlevel%

rem Dagitim ZIP'i: lisans metinleri EXE'nin yaninda da yer almalidir.
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Force -Path 'dist\EnglishCourseAI.exe','LICENSE','THIRD_PARTY_NOTICES.md' -DestinationPath 'dist\EnglishCourseAI-Windows.zip'"
if errorlevel 1 exit /b %errorlevel%

echo Built: %CD%\dist\EnglishCourseAI.exe
echo Release ZIP: %CD%\dist\EnglishCourseAI-Windows.zip

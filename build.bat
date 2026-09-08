@echo off
setlocal
cd /d "%~dp0"

rem Paketleme TEMIZ bir sanal ortamdan yapilmalidir. PYTHON degiskeniyle o
rem ortamin yorumlayicisini verin; aksi halde genel site-packages icindeki
rem ilgisiz kutuphaneler (pandas, lxml, ...) de EXE'ye girer.
rem   python -m venv %TEMP%\EnglishCourseAI-venv
rem   %TEMP%\EnglishCourseAI-venv\Scripts\pip install -r requirements.txt pyinstaller
rem   set "PYTHON=%TEMP%\EnglishCourseAI-venv\Scripts\python.exe" ^&^& build.bat
if "%PYTHON%"=="" set "PYTHON=python"

"%PYTHON%" -m PyInstaller --noconfirm --clean EnglishCourseAI.spec
if errorlevel 1 exit /b %errorlevel%

rem Dagitim ZIP'i: lisans metinleri EXE'nin yaninda da yer almalidir.
"%PYTHON%" tools\make_release_zip.py
if errorlevel 1 exit /b %errorlevel%

echo Built: %CD%\dist\EnglishCourseAI.exe
echo Release ZIP: %CD%\dist\EnglishCourseAI-Windows.zip

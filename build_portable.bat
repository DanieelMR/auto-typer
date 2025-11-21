@echo off
echo ============================================
echo   Generando ejecutable portable de Auto Typer
echo ============================================
echo.

echo Instalando PyInstaller...
pip install pyinstaller

echo.
echo Generando ejecutable...
pyinstaller --onefile --windowed --icon=NONE --name="AutoTyper" auto_typer.py

echo.
echo ============================================
echo   LISTO! El ejecutable esta en la carpeta dist/
echo ============================================
pause

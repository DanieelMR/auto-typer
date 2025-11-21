@echo off
echo ============================================
echo   Generando ejecutable OPTIMIZADO con Nuitka
echo   (Menor consumo de recursos)
echo ============================================
echo.

echo Instalando Nuitka y dependencias...
pip install nuitka zstandard ordered-set

echo.
echo NOTA: Este proceso puede tardar 5-10 minutos la primera vez
echo.
echo Compilando con Nuitka...
python -m nuitka --onefile --windows-disable-console --enable-plugin=tk-inter --output-filename=AutoTyper.exe auto_typer.py

echo.
echo ============================================
echo   LISTO! El ejecutable optimizado esta aqui
echo ============================================
pause

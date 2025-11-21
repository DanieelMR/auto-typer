@echo off
echo ============================================
echo   Ejecutable Portable OPTIMIZADO
echo   (PyInstaller con compresion)
echo ============================================
echo.

echo Instalando PyInstaller...
pip install pyinstaller

echo.
echo OPCIONAL: Instalando UPX para mayor compresion...
echo (Si falla, el ejecutable se creara igual, solo sera un poco mas grande)
winget install upx.upx 2>nul
echo.

echo Generando ejecutable optimizado...
pyinstaller --clean auto_typer_optimized.spec

echo.
echo ============================================
echo   LISTO! El ejecutable esta en: dist\AutoTyper.exe
echo   Ejecutable optimizado y comprimido
echo ============================================
pause

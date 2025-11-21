# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['auto_typer.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['keyboard', 'pyautogui'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'pandas', 'scipy', 'PIL'],  # Excluir librerías innecesarias
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AutoTyper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,  # Reduce tamaño eliminando símbolos de debug
    upx=True,    # Comprime el ejecutable (requiere UPX instalado)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Sin ventana de consola
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Omega Universal OS GUI Application
Builds a standalone executable with all dependencies bundled.
"""

block_cipher = None

a = Analysis(
    ['gui_app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'matplotlib',
        'matplotlib.backends.backend_qt5agg',
        'numpy',
        'utils',
        'ai_engine',
        'education',
        'healthcare',
        'governance',
        'economics',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='OmegaUniversalOS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window for GUI app
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon file path if available
)

# For macOS
app = BUNDLE(
    exe,
    name='OmegaUniversalOS.app',
    icon=None,
    bundle_identifier='com.omegasystems.universalos',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'NSPrincipalClass': 'NSApplication',
    },
)

#!/bin/bash
# Build script for creating standalone Omega Universal OS executable

echo "=========================================="
echo "Omega Universal OS - Build Script"
echo "=========================================="
echo ""

# Check if PyInstaller is installed
if ! python -c "import PyInstaller" 2>/dev/null; then
    echo "PyInstaller not found. Installing..."
    pip install pyinstaller
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/ *.spec 2>/dev/null

# Build the executable
echo ""
echo "Building standalone executable..."
pyinstaller omega_gui.spec

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "Build completed successfully!"
    echo "=========================================="
    echo ""
    echo "Executable location:"
    
    if [ -d "dist/OmegaUniversalOS.app" ]; then
        echo "  macOS: dist/OmegaUniversalOS.app"
    elif [ -f "dist/OmegaUniversalOS.exe" ]; then
        echo "  Windows: dist/OmegaUniversalOS.exe"
    elif [ -f "dist/OmegaUniversalOS" ]; then
        echo "  Linux: dist/OmegaUniversalOS"
    fi
    
    echo ""
    echo "You can now distribute the executable as a standalone application."
else
    echo ""
    echo "Build failed. Please check the error messages above."
    exit 1
fi

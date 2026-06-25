#!/bin/bash

#------------#
# build .exe #
#------------#
wine python -m PyInstaller "Crank It!.spec"
echo "Build .exe"

#----------------#
# build AppImage #
#----------------#
.venv/bin/pyinstaller "Crank It!.spec"
echo "Build AppImage"
mv "dist/Crank_It!" dist/Crank_It!.AppImage

#------------------------#
# Remove Build directory #
#------------------------#
rm -rf build/
rm -rf __pycache__

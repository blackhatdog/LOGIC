@echo off
color 0b
title pyinstaller builder for python3.10

pyinstaller --onefile -w --exclude-module _bootlocale pkg.py


@echo off
@echo **********************************************
@echo ****  FirstAidKit information extractor   ****
@echo ****  Developed by github.com/ehboudjema  ****
@echo ****  V1.0 - all rights reserved - 2020   ****
@echo **********************************************
@echo.
@echo.
@echo.
@echo.
@echo Exctacting all file names from your system, this may take few minutes ...
dir /s /b c:\ > info.txt
@echo Exctacting running programs on your system...
wmic  PROCESS get /all >> info.txt
@echo Extracting stratup programs...
wmic startup >> info.txt
@echo Extracting active network connections...
netstat -nao >> info.txt
@echo Extraction finished succefully. All data is stored in the file: info.txt.
@echo.
@echo.
@echo.
@echo.
@echo Press Enter to close this window.
pause


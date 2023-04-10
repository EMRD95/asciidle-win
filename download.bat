@echo off
set /P choice="Do you want to populate the txt folder with Pinups (y/n)? "
if /I "%choice%"=="y" (
    echo Downloading Pinups...
    powershell -Command "Invoke-WebRequest -Uri 'https://files.catbox.moe/ykkxlt.zip' -OutFile 'Pinups.zip'"
    echo Extracting Pinups...
    powershell -Command "Expand-Archive -Path 'Pinups.zip' -DestinationPath '.'"
    echo Deleting the zip file...
    del Pinups.zip
    echo Done!
) else (
    echo Quitting...
    exit /B
)

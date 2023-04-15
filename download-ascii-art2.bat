@echo off
set "txt_folder=txt"
if exist "%txt_folder%\anime$$.txt" (
    echo Files already exist. Skipping download and extraction.
) else (
    echo Downloading ASCII art...
    powershell -Command "Invoke-WebRequest -Uri 'https://files.catbox.moe/gvl6lb.zip' -OutFile 'txt.zip'"
    echo Extracting ASCII art...
    powershell -Command "Expand-Archive -Path 'txt.zip' -DestinationPath '.'"
    echo Deleting the zip file...
    del txt.zip
    echo Done!
)

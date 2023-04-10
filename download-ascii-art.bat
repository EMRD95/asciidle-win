@echo off
set "txt_folder=txt"
if exist "%txt_folder%\pinups$$.txt" (
    echo Pinups already exist. Skipping download and extraction.
) else (
    echo Downloading Pinups...
    powershell -Command "Invoke-WebRequest -Uri 'https://files.catbox.moe/ykkxlt.zip' -OutFile 'Pinups.zip'"
    echo Extracting Pinups...
    powershell -Command "Expand-Archive -Path 'Pinups.zip' -DestinationPath '.'"
    echo Deleting the zip file...
    del Pinups.zip
    echo Done!
)

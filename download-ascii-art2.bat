@echo off
set "txt_folder=txt"
set "expected_sha256=732AE6C1B519DF97C8101D79BEDEDD4FED74A0AB704B28DF926A66BB07A7649D"

if exist "%txt_folder%\anime$$.txt" (
    echo Files already exist. Skipping download and extraction.
) else (
    echo Downloading ASCII art...
    powershell -Command "Invoke-WebRequest -Uri 'https://files.catbox.moe/gvl6lb.zip' -OutFile 'txt.zip'"
    
    echo Verifying checksum...
    powershell -Command "$actual_sha256 = Get-FileHash -Path 'txt.zip' -Algorithm SHA256; if ($actual_sha256.Hash -ne '%expected_sha256%') { Write-Error ('Checksum verification failed. Expected: {0}, Actual: {1}. Aborting.' -f '%expected_sha256%', $actual_sha256.Hash); exit 100 }"
    
    if errorlevel 100 (
        echo Checksum verification failed. Removing the zip file...
        del txt.zip
        echo Zip file removed. Exiting.
    ) else (
        echo Extracting ASCII art...
        powershell -Command "Expand-Archive -Path 'txt.zip' -DestinationPath '.'"
    
        echo Deleting the zip file...
        del txt.zip
    
        echo Done!
    )
)

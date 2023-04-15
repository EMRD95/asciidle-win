@echo off
set "txt_folder=txt"
set "expected_sha256=63644D4252E59912398FC13B906FAACE0DE9E19DF92C771DA3A81C109475A7B1"

if exist "%txt_folder%\pinups$$.txt" (
    echo Pinups already exist. Skipping download and extraction.
) else (
    echo Downloading Pinups...
    powershell -Command "Invoke-WebRequest -Uri 'https://files.catbox.moe/ykkxlt.zip' -OutFile 'Pinups.zip'"
    
    echo Verifying checksum...
    powershell -Command "$actual_sha256 = Get-FileHash -Path 'Pinups.zip' -Algorithm SHA256; if ($actual_sha256.Hash -ne '%expected_sha256%') { Write-Error ('Checksum verification failed. Expected: {0}, Actual: {1}. Aborting.' -f '%expected_sha256%', $actual_sha256.Hash); exit 100 }"
    
    if errorlevel 100 (
        echo Checksum verification failed. Removing the zip file...
        del Pinups.zip
        echo Zip file removed. Exiting.
    ) else (
        echo Extracting Pinups...
        powershell -Command "Expand-Archive -Path 'Pinups.zip' -DestinationPath '.'"
    
        echo Deleting the zip file...
        del Pinups.zip
    
        echo Done!
    )
)

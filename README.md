# asciidle-win
Asciidle for windows in C++. This small program lets you display ASCII art in your terminal (cmd or powershell) with some configurations available.

To compile the C++ program :

Install Visual Studio Build Tools 2019 with "Desktop development with C++"

Open Developer Command Prompt for VS 2019 (with Administrator rights) and cd to the folder containing asciidle.cpp

rc /r app_resources.rc

cl /EHsc asciidle.cpp app_resources.res /link /out:asciidle.exe

You can use the python configuration GUI as it is or make it an executable too :

pip install pyinstaller

pyinstaller --onefile --noconsole asciidle-config.py

After running the command, you will find the .exe file in the dist folder created in the same directory as your Python script. Move it to the main folder.

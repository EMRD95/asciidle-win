# asciidle-win

Asciidle for windows in C++. This small program lets you display ASCII art in your terminal (cmd or powershell) with some configurations available.

You can just download `Asciidle` from the [release](https://github.com/EMRD95/asciidle-win/releases/tag/asciidle), it's preconfigured and works directly. You can still configure it as wanted from the configuration panel.

## To compile the C++ program:

1. Install Visual Studio Build Tools 2019 with "Desktop development with C++"
2. Open Developer Command Prompt for VS 2019 (with Administrator rights) and cd to the folder containing asciidle.cpp
3. `rc /r app_resources.rc`
4. `cl /EHsc asciidle.cpp app_resources.res /link /out:asciidle.exe`

## You can use the python configuration GUI as it is or make it an executable too:

1. `pip install pyinstaller`
2. `pyinstaller --onefile --noconsole --icon=res/asciidle-config.ico asciidle-config.py`

After running the command, you will find the .exe file in the dist folder created in the same directory as your Python script. Move it to the main folder to set up configuration.

## Compile an installer for the program

The installer is made with Inno Setup, it automatically set the path to the txt directory to the installation folder.
Simply [download Inno Setup](https://jrsoftware.org/isdl.php) and build the installer with the .iss script.

## For asciidle to work, set the path to your ASCII art folder accordingly.

![image](https://user-images.githubusercontent.com/114953576/232246732-029e321d-423d-49a6-ad07-e49b49d5fdfb.png)

## You can also set asciidle to PATH so it runs from any command line (cmd or powershell) by typing "asciidle"

![image](https://user-images.githubusercontent.com/114953576/232230415-6c72d002-5166-4177-9d94-0b43347a2f9f.png)

You can also run the program directly by executing asciidle.exe.

To automatically download some old school ASCII art, run download-ascii-art.bat directly or from asciidle-config.exe (NSFW).

It works for ASCII arts but also ASCII stories.

https://user-images.githubusercontent.com/114953576/232248764-224c731b-2918-4339-9411-f8c5d1e3ba84.mp4

## Note

In this repository, you will find a C++ program and a Python script that display and configure ASCII art in a console window. When compiled or bundled as executables, these programs might generate false positives with certain antivirus software due to the necessary use of specific functions and libraries, such as Windows API functions like **GetModuleFileName**, **FindFirstFile**, and **GetStdHandle** in the C++ program and **os**, **sys**, **ctypes**, and **tkinter** in the Python script. These functions are often associated with malware but are essential for the intended functionality of the programs in this repository.

## Credits

Thanks to http://www.textfiles.com/art/ for providing a well maintained archive of ASCII arts.

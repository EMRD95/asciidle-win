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

After running the command, you will find the .exe file in the dist folder created in the same directory as your Python script. Move it to the main folder to set up configuration.

For asciidle to work, set the path to your ASCII art folder accordingly.

![image](https://user-images.githubusercontent.com/114953576/230944421-0e454102-b69f-4761-9a36-079e0acd831c.png)

You can also set asciidle to PATH so it runs from any command line (cmd or powershell) by typing "asciidle"

![image](https://user-images.githubusercontent.com/114953576/230939010-e973b1eb-bb88-4841-95cc-24ff50adf40a.png)

You can also run the program directly by executing asciidle.exe

To make things more spicy, you can automatically download some old school ASCII art by running download-ascii-art.bat

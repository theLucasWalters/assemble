**This is meant for x64 Windows machines with masm32 installed*

# Python Assemble Module
I don't know if I can actually call this a module, but whatever.

Basically, assembling Assembly files is hard on Windows. Now it's not. Have fun!

## How I use this
I use `pyinstaller --onefile assemble.py` to build this program into an executable. If you don't know how to add a `.exe` to your path (to use as a command in your terminal), follow the following steps:

## Add to your path
Open Settings. `Go to System > About > Advanced System Settings > Environment Variables > User Variables > PATH`\
Click on `Edit > New` and add `C:/path/to/assemble`, but don't add the actual `assemble.exe` file.\
After that, start a new instance of your terminal and type `assemble`. It should work just fine!

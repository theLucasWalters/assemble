# Python Assemble Module
I don't know if I can actually call this a module, but whatever.

Basically, assembling Assembly files is hard on Windows. Now it's not. Have fun!

## How I use this
I use `pyinstaller --onefile assemble.py` to build this program into an executable. If you don't know how to add a `.exe` to your path (to use as a command in your terminal), follow the following steps:

## Add to your path
Open Settings. Go to `System` > `About` > `Advanced System Settings` > `Environment Variables` > `User Variables` > `PATH`\
Click on `Edit` > `New` and add `C:/path/to/assemble/executable`, but don't add the actual `assemble.exe` file.\
After that, start a new instance of your terminal and type `assemble`. It should work just fine!

## Dependencies
### System
x86_32 Windows\
x64 Windows

### Programs
masm32
- If you don't have masm32 installed, get it at [masm32.masmcode.com/masm32](http://masm32.masmcode.com/masm32/) or download v11 directly with this link: [masm32v11r.zip](http://masm32.masmcode.com/masm32/masm32v11r.zip)

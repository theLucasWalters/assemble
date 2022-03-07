# imports
import os
import sys

# variables to make things simpler for myself
osys    = os.system
sysargs = sys.argv

# main
def main():

    # check that a file was actually input
    try:
        file = sysargs[1]
    except:
        # if not, throw an error
        print("Enter the file you want to assemble.")
        quit()

    # call parse() to get the file name (fn) and the file extension (ext)
    fn, ext = parse(file)

    # it needs to be an assembly file, otherwise it won't work
    if ext != 'asm':
        print("The input file must be a '.asm' file.")
        quit()

    # define the commands
    cmd1 = f'/masm32/bin/ml /c /Zd /coff {fn}.asm'
    cmd2 = f'/masm32/bin/Link /SUBSYSTEM:CONSOLE {fn}.obj'

    # call the commands
    osys(cmd1)
    osys(cmd2)

# function to parse the file name at the '.'
def parse(file):
    fn, ext = file.split('.')
    return fn, ext

# because this is meant to run in the console
if __name__ == "__main__":
    main()

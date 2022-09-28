"""
List of packages able to install:
Dolphin
Silver
"""
########
# reqs #
########
from termcolor import cprint
from os import system


def welcome():
    cprint("----- Welcome to Proc Package manager -----", "green")
    print("")
    print("")
    print("To install a package run \"proc install <package name>\"!")
def install(package):
    # Add a new file for this but for now this is fine
    if package == "Dolphin":
        system("cd")
        system("git clone https://www.github.com/Ubuntufanboy/Dolphin.git")
        system("cd Dolphin")
        system("bash ./install.sh")
        system("cd")
        # Add Dolphin as an alias to .bashrc
        system("echo alias Dolphin=\"cd ~/Dolphin/Dolphin && python3 runthis.py\")
        print("Dolphin has been installed! run \"Dolphin\" to run it!")
    elif package == "Silver":
        print("Installing Silver")
        system("cd")
        # TODO: Make a dir with all installed packages and put them in that folder
        system("wget https://raw.githubusercontent.com/Ubuntufanboy/Silver/main/silver.py")
        print("Silver has been installed")
def verify(command):
    tokened = command.split()
    if tokened[0] == "proc" and tokened[1] == "install":
        pass
    else:
        return False
    try:
        print(f"Error! invalid command {tokened[3]})
        return False
    except:
        return True
welcome()
while 1:
    print("This is the proc shell! run a command here!")
    command = input(">>> ")
    if verify(command):
        foo = command.split()
        install(foo[2])
    else:
        print("Install failed! invalid command")

# =============
# DOS in Python
# =============

# Python Modules

import os
import subprocess
import string

# Sets current directory to where the boot.py is

os.chdir(os.path.dirname(__file__))

# Custom Modules
import com
import about
import edit
import files
import system

# About OS

dos_ver = "6.0 beta 2"

# Default Directories
root_dir = os.path.dirname(__file__)

# Initialisation
command = 0

def boot():
    boot_string = (" PY-DOS Command Prompt "+str(dos_ver))

    boot_equals = "="
    for i in range(len(boot_string)):
        boot_equals = boot_equals+"="
    
    print(boot_equals)
    print(boot_string)
    print(boot_equals)
    #print("This OS is running from '"+root_dir+"'")

    if intro_needed == 1:
        about.about()
        com.com()
    else:
        print("")
        com.com()

# SYSTEM.INI
intro_needed = 0
try:
    conf_dir = os.getcwd()+"/config" 

    f= open(conf_dir+"/system.ini","r")
    system_ini = f.readlines()
    vers = []
    loop = 0
    for i in range(len(system_ini)):
        if "ver" in system_ini[loop]:
            vers.append(system_ini[loop])
        loop = loop+ 1
    
    loop = 0
    for lines in vers:
        vers[loop] = vers[loop].strip("ver ")
        vers[loop] = vers[loop].strip("\n")
        loop = loop + 1
        
    
    f.close()
    
    with open(conf_dir+"/system.ini","w") as f:
        system_ini[0] = "ver "+str(dos_ver)+"\n"
        system_ini[1] = "prompt 0\n"
        system_ini[2] = "prompt 0\n"
        system_ini[3] = system_ini[3]
        f.writelines(system_ini)
    intro_needed = 0

except FileNotFoundError:
    os.mkdir("config")
    conf_dir = os.getcwd()+"/config"
    with open(conf_dir+"/system.ini","w") as f:
        system_ini = []
        system_ini.append("ver "+str(dos_ver)+"\n")
        system_ini.append("prompt 0\n")
        system_ini.append("prompt 0\n")
        system_ini.append("user "+os.getlogin()+"\n")
        f.writelines(system_ini)
    intro_needed = 1


except FileExistsError:
    conf_dir = os.getcwd()+"/config"
    with open(conf_dir+"/system.ini","w") as f:
        system_ini = []
        system_ini.append("ver "+str(dos_ver)+"\n")
        system_ini.append("prompt 0\n")
        system_ini.append("prompt 0\n")
        system_ini.append("user "+os.getlogin()+"\n")
        f.writelines(system_ini)
    intro_needed = 1

boot()

try:  
    #boot()
    print("")

except SystemExit:

    exit()

except:
    os.system("cls")
    os.system("color 17")
    print("SYSTEM ERROR")
    print("")
    print("A fatal exception has occured")
    print("")
    
    print("* Press any key to terminate this application")
    print("* Press Enter to quit PY-DOS")
    print("")

    choice = input()

    if choice != "":
        os.system("cls")
        boot()
    else:
        exit()

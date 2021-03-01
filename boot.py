# =============
# DOS in Python
# =============

# Python Modules

import os
import subprocess
import string

# Custom Modules
import com
import about

# SYSTEM.TXT
intro_needed = 0
try:
    f= open("runonce","r")
    intro_needed = 0

except FileNotFoundError:
    f= open("runonce","w")
    f.write("1")
    intro_needed = 1
    f.close
    
# About OS
dos_ver1 = 2
dos_ver2 = 0
dos_ver_str = str(dos_ver1)+"."+str(dos_ver2)

# Default Directories
root_dir = os.getcwd()
current_dir = root_dir
new_dir = current_dir

# Initialisation
prompt = current_dir+"> "
command = 0

def boot():
    boot_string = (" DOS Command Prompt "+dos_ver_str)
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

boot()


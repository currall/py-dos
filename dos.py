# =============
# DOS in python
# =============

# Python Modules

import os
import subprocess
import string

# Custom Modules

import dir
import help
import edit

# SYSTEM.TXT
intro_needed = 0
try:
    f= open("system.txt","r")
    intro_needed = 0

except FileNotFoundError:
    f= open("system.txt","w")
    f.write("1")
    intro_needed = 1
    f.close
    
# About OS
dos_ver1 = 1
dos_ver2 = 1
dos_ver_str = str(dos_ver1)+"."+str(dos_ver2)

def getver():
    dos_ver1 = dos_ver1
    dos_ver2 = dos_ver2

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
        help.about()
        restart()
    else:
        print("")
        com()

def restart():
    com()
    
def com(): # Command Prompt
    
    try:
        
        current_dir = os.getcwd()
        prompt = current_dir+"> "
        prompt = prompt.upper()
        command = input(prompt)
        command = command.casefold()

        #boot
        if command == "boot":
            boot()
        elif command == "command":
            restart()
        
        # dir
        elif "dir" in command and command[0] == "d":
            dir.dir(command)
            restart()

        elif command == "disks" or command == "fdisk":
            disks()

        elif command[0] == "c" and command[1] == "d":
            if command[3] == ".":
                updir()
            else:
                cd(command)
        elif command[0] == "m" and command[1] == "d":
            md(command)

        elif command[0] == "r" and command[1] == "d":
            rd(command)

        elif command[0] == "d" and command[1] == "e" and command[2] == "l":
            delete(command)
                
        elif command[1] == ":":
            drive(command[0])

        elif command == "ver":
            ver()
        elif command == "about":
            help.about()
            restart()
            
        elif "help" in command and command[0] == "h":
            help.help(command)
            restart()

        elif command == "cls":
            cls()

        elif command[0] == "t" and command[1] == "y" and command[2] == "p" and command[3] == "e": #type
            edit.type(command)
            restart()

        elif command[0] == "e" and command[1] == "d" and command[2] == "i" and command[3] == "t": #edit
            edit.edit(command)
            restart()
            
        elif command[0] == "r" and command[1] == "e" and command[2] == "n": #ren
            rename(command)

        elif command[0] == "c" and command[1] == "o" and command[2] == "p" and command[3] == "y": #copy
            copy(command)
        
        # error  
        elif "exe" in command:
            exe(command)

        elif command == "exit":
            exitq = input("Are you sure you want to exit DOS? [Y/N]: ")
            if exitq == "y" or exitq == "Y":
                exit()
            else:
                restart()
        
        else:
            if os.path.isfile(command+".exe") == True:
                subprocess.Popen(command+".exe")
                restart()
            else:
                print("Error: Command not found")
                restart()

            
    except IndexError:
        print("Error: Command not found")
        restart()

def exe(exe_command): # Executable Launcher
    #print("exe")
    try:

        if exe_command[0] == "e" and exe_command[1] == "x" and exe_command[2] == "e":
            exe_char = int(len(exe_command)-5)
            #print(next_dir_char)
            exe_loop = 4
            exe = exe_command[4]
            for i in range(exe_char):
                exe_loop = exe_loop + 1
                exe = exe + exe_command[exe_loop]

            if ".exe" not in exe:
                exe = exe+".exe"
            subprocess.Popen(exe)
        else:
            subprocess.Popen(exe_command)
        
    except IndexError:
        print("Error: Must specify executable")

    except FileNotFoundError:
        print("Error: Executable not found")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: Executable not found")

    com()

def drive(drive_select): # Drive Selection

    drive_select = drive_select+":\\"
    os.chdir(drive_select)

    com()

def copy(copy_command):
    os.system(copy_command)

    com()

def disks():
    drives = []
    
    for l in string.ascii_uppercase:
        if os.path.exists(l+":\\"):
            drives.append(l)
    print("There are "+str(len(drives))+" hard drive(s) installed:")
    print(drives)

    com()
  


def cd(cd_command):
    #print(cd_command)
    try:
        next_dir_char = int(len(cd_command)-4)
        #print(next_dir_char)
        next_dir_loop = 3
        next_dir = cd_command[3]
        for i in range(next_dir_char):
            next_dir_loop = next_dir_loop + 1
            next_dir = next_dir + cd_command[next_dir_loop]

        current_dir = os.getcwd() 
        #print(next_dir)
        #next_dir = input("Change Directory to: ")
        next_dir = current_dir+"\\"+next_dir
        os.chdir(next_dir)
        
    except OSError:
        print("Error: Directory not found")

    except IndexError:
        print("Error: Must specify directory")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: Directory not found")

    com()

def updir():
    os.chdir("..")

    com()

def md(md_command):
    try:
        make_dir_char = int(len(md_command)-4)
        #print(make_dir_char)
        make_dir_loop = 3
        make_dir = md_command[3]
        for i in range(make_dir_char):
            make_dir_loop = make_dir_loop + 1
            make_dir = make_dir + md_command[make_dir_loop]
        
        #make_dir = input("Enter new directory name: ")
        os.mkdir(make_dir)
    except FileExistsError:
        print("Error: Directory already exists")

    except IndexError:
        print("Error: Must specify directory")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: Directory not found")

    com()

def rd(rd_command):
    try:
        rem_dir_char = int(len(rd_command)-4)
        #print(make_dir_char)
        rem_dir_loop = 3
        rem_dir = rd_command[3]
        for i in range(rem_dir_char):
            rem_dir_loop = rem_dir_loop + 1
            rem_dir = rem_dir + rd_command[rem_dir_loop]
            
        #rem_dir = input("Enter directory to delete: ")
        os.rmdir(rem_dir)

    except FileNotFoundError:
        print("Error: Directory not found")

    except IndexError:
        print("Error: Must specify directory")

    except OSError:
        print("Error: This directory is not empty")

    except:
        print("Error: Directory not found")

    com()

def delete(del_command):
    try:
        del_char = int(len(del_command)-5)
        #print(make_dir_char)
        del_loop = 4
        del_file = del_command[4]
        for i in range(del_char):
            del_loop = del_loop + 1
            del_file = del_file + del_command[del_loop]

        ensure = input("Are you sure you want to delete this file? [Y/N]: ")
        if ensure == "y" or "Y":  
            os.remove(del_file)

    except PermissionError:
        print("Error: You do not have permission to delete this file")

    except FileNotFoundError:
        print("Error: File not found")

    except IndexError:
        print("Error: Must specify file")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: File not found")

    com()

def rename(ren_command):
    
    try:
        ren_char = int(len(ren_command)-5)
        #print(make_dir_char)
        ren_loop = 4
        ren_file = ren_command[4]
        for i in range(ren_char):
            ren_loop = ren_loop + 1
            ren_file = ren_file + ren_command[ren_loop]

        
        #print(len(ren_file))
        #print(ren_file.index("."))
        #print(ext_len)
        if ren_file.find(".") != -1:
            
            ext_len = len(ren_file) - (ren_file.index("."))
            
            file_extension = "."
            ext_loop = ren_file.find(".") + 1
            for i in range(ext_len - 1):
                file_extension = file_extension + ren_file[ext_loop]
                ext_loop = ext_loop + 1
            #print(file_extension)
        
            new_name = input("Enter new file name: ")
            if file_extension not in new_name:
                new_name = new_name+file_extension
        
            os.rename(ren_file,new_name)
        else:
            new_name = input("Enter new file name: ")
            os.rename(ren_file,new_name)

        
    except PermissionError:
        print("Error: You do not have permission to edit this file")

    except FileNotFoundError:
        print("Error: File not found")

    except IndexError:
        print("Error: Must specify file")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: File not found")

    com()
        
def ver():
    print("DOS Version: "+dos_ver_str)

    com()

def cls():
    os.system("cls")

    com()


boot()


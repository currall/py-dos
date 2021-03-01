import os
import subprocess
import time

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

    com.com()

def clock():
    current_time = time.strftime("%H:%M:%S", time.gmtime())
    current_date = time.strftime("%d-%m-%Y", time.gmtime())
    print("Time: "+current_time)
    print("Date: "+current_date)
    
def ver():
    print("DOS Version: "+dos_ver_str)

    com.com()

def cls():
    os.system("cls")

    com.com()

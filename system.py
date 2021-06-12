import os
import subprocess
import time
import platform
import sys

import about

root_dir = os.getcwd()

def exe(exe_command): # Windows Executable Launcher
    try:

        if exe_command[:3] == "exe":
            exe = exe_command.replace("exe ","")

            if ".exe" not in exe:
                exe = exe+".exe"
                
            subprocess.Popen(exe)
            
        else:
            subprocess.Popen(exe_command)
        
    except IndexError:
        print("Error: Must specify executable")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: Executable not found")

def cmd(cmd_command): # CMD Command
    try:
        cmd_str = cmd_command.replace("cmd ","")

        os.system(cmd_str)
    except:
        print("Error: 'CMD' command not found")

def py(py_command):
    try:
        if py_command[:3] == "py ":
            py_str = py_command.replace("py ","")

            if ".py" not in py_command:
                py_str = py_str + ".py"
            
            os.system("py "+py_str)
        
        else:
            os.system("py "+py_command)

    except:
        print("Error: Python file not found")

def clock(clock_type):
    
    current_time = time.strftime("%H:%M:%S", time.gmtime())
    current_date = time.strftime("%d-%m-%Y", time.gmtime())
    if clock_type == "t":
        print("Time: "+current_time)
    elif clock_type == "d":
        print("Date: "+current_date)
    else:
        print("Time: "+current_time)
        print("Date: "+current_date)

def echo(echo_command):
    
    echo_str = echo_command.replace("echo ","")
    print(echo_str)

def ver():

    f= open(root_dir+"/config/system.ini","r")
    system_ini = f.readlines()

    loop = 0
    
    for i in range(len(system_ini)):
        if "ver" in system_ini[loop]:
            ver = system_ini[loop]
        loop = loop+ 1
    
    ver = ver.replace("ver ","")
    ver = ver.replace("\n","")

    loop = 0
    
    for i in range(len(system_ini)):
        if "user" in system_ini[loop]:
            user = system_ini[loop]
        loop = loop+ 1

    user = user.replace("user ","")
    user = user.replace("\n","")

    f.close()

    print(user)
    equals = "="
    for i in range( len(user) - 1):
        equals = equals + "="
    print(equals)
    print("OS:              "+platform.system()+" "+platform.release())
    print("OS Version:      v"+platform.version())
    print("PY-DOS Version:  "+str(ver))
    
def oldver():
    
    f= open(root_dir+"/config/system.ini","r")
    system_ini = f.readlines()
    
    loop = 0

    for i in range(len(system_ini)):
        if "ver" in system_ini[loop]:
            ver = system_ini[loop]
        loop = loop+ 1
    
    ver = ver.replace("ver ","")
    ver = ver.replace("\n","")

    f.close()
        
    print("DOS Version: "+ver)

def setver(sv_command):

    sv_str = sv_command.replace("setver ","")
    new_dos_ver = sv_str

    f= open(root_dir+"/config/system.ini","r")
    system_ini = f.readlines()
    f.close()
    with open(root_dir+"/config/system.ini","w") as f:
        system_ini[0] = "ver "+str(new_dos_ver)+"\n"
        f.writelines(system_ini)

def prompt(prompt_command):
    prompt_str = prompt_command.replace("prompt ","")

    f= open(root_dir+"/config/system.ini","r")
    system_ini = f.readlines()
    f.close()
    print(prompt_str)
    with open(root_dir+"/config/system.ini","w") as f:
        system_ini[1] = "prompt 1\n"
        system_ini[2] = "prompt "+prompt_str+"\n"
        f.writelines(system_ini)

def cls():
    
    os.system("cls")

def clip(clip_command):
    clip_text = clip_command.replace("clip ", "")
    with open(root_dir+"/config/clipb.ini","a") as f:
        f.write(clip_text+"\n")

def paste():
    try:
        f = open(root_dir+"/config/clipb.ini","r")
        clipboard = f.readlines()
        f.close()
        
        clipboard_length = len(clipboard)

        paste_text = clipboard[clipboard_length - 1]
        paste_text = paste_text.replace("\n", "")

        print(paste_text)
    except:
        print("Error: Nothing copied yet!")

def color(color_command):

    os.system(color_command)

    # RESET

    if color_command == "color reset":
        os.system("color")

def username(un_command):

    if un_command[:5] == "uname":
        un_str = un_command.replace("uname ","")
    if un_command[:8] == "username":
        un_str = un_command.replace("username ","")
    new_uname = un_str

    f= open(root_dir+"/config/system.ini","r")
    system_ini = f.readlines()
    f.close()
    with open(root_dir+"/config/system.ini","w") as f:
        system_ini[3] = "user "+str(new_uname)+"\n"
        f.writelines(system_ini)

def shutdown(sd_command):

    if sd_command == "shutdown r":
        os.system("shutdown -r")
    elif sd_command == "shutdown h":
        os.system("shutdown -h")
    else:
        os.system("shutdown -s")
    
    print("You will be signed out in under 1 minute")
    cancel = 0
    while cancel != 1:
        cancl = input("Type 'ABORT' to cancel: ").upper()
        if cancl == "abort" or cancl == "ABORT":
            os.system("shutdown -a")
            os.system("cls")
            print("Shutdown aborted.")
            cancel = 1


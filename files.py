import os
import subprocess
import string
import shutil

import com

def dir(dir_command):
    
    temp_dir = os.getcwd()
    files = os.listdir(temp_dir)
    if "__pycache__" in files:
        files.remove("__pycache__")
    
    if("/w" in dir_command):
        print(files)
    elif("/s" in dir_command):
        dir_command.index("/")
        if int(dir_command.index("/")) == int(dir_command.index("s")-1):
            searched_dir = []
            
            dir_search_len = len(dir_command) - int(dir_command.index("s")+2)
            loop = int(dir_command.index("s")+3)
            
            search_term = dir_command[int(dir_command.index("s")+2)]
            
            for i in range(dir_search_len - 1):
                search_term = search_term + dir_command[loop]
                loop = loop+1
            print(search_term)
            for s in files:
                if search_term in s:
                    searched_dir.append(s)
            print(searched_dir)
    else:
        x = 0
        for i in range(len(files)):
            print(files[x])
            x = x + 1
            
def drive(drive_select): # Drive Selection

    drive_select = drive_select+":\\"
    os.chdir(drive_select)

    com.com()

def disks():
    drives = []
    
    for l in string.ascii_uppercase:
        if os.path.exists(l+":\\"):
            drives.append(l)
    print("There are "+str(len(drives))+" hard drive(s) installed:")
    print(drives)

    com.com()
  
def copy(copy_command):
    try:
        copy_file = copy_command.replace("copy ","")
        copy_folder = input("Enter folder to copy to: ")
        shutil.copyfile(copy_file,copy_folder+"//"+copy_file)

    except OSError:
        print("Error: File or Directory not found")

    except IndexError:
        print("Error: Must specify file or directory")

    except FileExistsError:
        print("Error: File already exists")

    except:
        print("Error: File or Directory not found")

    com.com()

def move(move_command):
    try:
        move_file = move_command.replace("move ","")
        move_folder = input("Enter folder to move to: ")
        shutil.copyfile(move_file,move_folder+move_file)
        
        ensure = input("Are you sure you want to delete this file? [Y/N]: ")
        if ensure == "y" or "Y":  
            os.remove(move_file)
        else:
            os.remove(move_folder+move_file)

    except OSError:
        print("Error: File or Directory not found")

    except IndexError:
        print("Error: Must specify file or directory")

    except FileExistsError:
        print("Error: File already exists")

    except:
        print("Error: File or Directory not found")

    com.com()
    
def cd(cd_command):
    #print(cd_command)
    try:
        if cd_command[:2] == "cd":
            next_dir = cd_command.replace("cd ","")
        elif cd_command[:5] == "chdir":
            next_dir = cd_command.replace("chdir ","")
        
        current_dir = os.getcwd() 
        #print(next_dir)
        #next_dir = input("Change Directory to: ")
        next_dir = current_dir+"\\"+next_dir
        os.chdir(next_dir)
        
    except OSError:
        print("Error: Directory not found")

    except IndexError:
        print("Error: Must specify directory")

    except:
        print("Error: Directory not found")

    com.com()
    
def updir():
    os.chdir("..")

    com.com()

def md(md_command):
    try:
        if md_command[:2] == "md":
            make_dir = md_command.replace("md ","")
        elif md_command[:5] == "mkdir":
            make_dir = md_command.replace("mkdir ","")
        
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

    com.com()

def rd(rd_command):
    try:
        if rd_command[:2] == "rd":
            rem_dir = rd_command.replace("rd ","")
        elif rd_command[:5] == "rmdir":
            rem_dir = rd_command.replace("rmdir ","")
            
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

    com.com()

def delete(del_command):
    try:
        del_file = del_command.replace("del ","")

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

    com.com()

def rename(ren_command):
    
    try:
        ren_file = ren_command.replace("ren ","")
        
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

    com.com()


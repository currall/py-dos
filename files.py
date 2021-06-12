import os
import subprocess
import string
import shutil
import datetime
import zipfile
import pathlib

import com

root_dir = os.getcwd()

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
        print("Type   Date Modified     Name")
        print("====   =============     ====")

        for i in range(len(files)):
            if os.path.isdir(files[x]) == True:

                dir = files[x]

                time = datetime.datetime.fromtimestamp(os.stat(files[x]).st_ctime)
                time = str(time)

                time = time.replace(time[-10:], "")
                
                print("dir    "+ time + "  "+ dir)
            x = x + 1
        x = 0
        for i in range(len(files)):
            if os.path.isfile(files[x]) == True:

                file = files[x]

                if file[-4:] == ".exe":
                    type = "exe    "
                elif file[-4:] == ".txt":
                    type = "text   "
                elif file[-4:] == ".zip":
                    type = "zip    "

                else:
                    type = "file   "

                time = datetime.datetime.fromtimestamp(os.stat(files[x]).st_ctime)
                time = str(time)

                time = time.replace(time[-10:], "")

                print(type + time + "  " + file)
            x = x + 1

def find(dir_command):
    search_term = dir_command.replace("find ","")
    #print(search_term)
    searched_dir = []

    temp_dir = os.getcwd()
    files = os.listdir(temp_dir)

    loop = 0
    
    for s in files:
        if search_term in s:
            searched_dir.append(s)
    print(searched_dir)

def fdisk(chkd_command):

    def fdisk_intro():

        os.system("cls")

        print("PY-DOS Disk Manager 2.0")
        print("")
        print("Choose one of the following:")
        print("")
        print("1: View Disk Partitions")
        print("2: Change current disk")
        print("3: View Disk Usage")
        print("")
    
    def choicef():
        
        try:
            choice = int(input("Enter choice: "))
            print("")
            options(choice)
        except FileNotFoundError:
            choicef()

    def options(choice):

        if choice == 1:
            disks()

        elif choice == 2:
            disk = input("Enter Disk Letter: ")
            try:
                disk = disk.upper()+":\\"
                os.chdir(disk)
            except:
                print("Disk not found")
                choicef()

        elif choice == 3:

            drives = []
            
            for l in string.ascii_uppercase:
                if os.path.exists(l+":\\"):
                    drives.append(l+":\\")
            loop = 0
            for i in range(len(drives)):
                total, used, free = shutil.disk_usage(drives[loop])
                print(drives[loop])
                print("Total Capacity: "+str(total // 1000000000)+"GB")
                print("Used: "+str(used // 1000000000)+"GB")
                print("Remaining: "+str(free // 1000000000)+"GB")
                print("")
                loop = loop + 1
        
        else:
            print("Incorrect Choice.")
            choice()
    
    fdisk_intro()
    choicef()    

def file2bin(bin_command):
    bin_file = bin_command.replace("2bin ","")

    if bin_file.find(".") != -1:
        new_bin_file = bin_file[:bin_file.index(".")]
    
    os.rename(bin_file,new_bin_file+".bin")

def comp(dskc_command):

    comp_dir = dskc_command.replace("comp ","")

    try:
        current_dir = os.getcwd()
        current_dir_contents = os.listdir(current_dir)
        comp_dir_contents = os.listdir(comp_dir)

        loop = 0

        #print(current_dir_contents)
        #print(comp_dir_contents)

        print("")
        comp_results = []
        comp_results2 = []
        
        for i in range(len(current_dir_contents)):
            if not current_dir_contents[loop] in comp_dir_contents:
                comp_results.append(current_dir_contents[loop])
                loop = loop + 1
        loop2 = 0
        for i in range(len(comp_dir_contents)):
            if not comp_dir_contents[loop2] in current_dir_contents:
                comp_results2.append(comp_dir_contents[loop2])
                loop2 = loop2 + 1
                
        if comp_results == [] and comp_results2 == []:
            print("Directories match")
        else:
            print("In current directory but not '"+comp_dir+"':")    
            print(comp_results)
            print("")
            print("In '"+comp_dir+"' but not current directory:")    
            print(comp_results2)

    except OSError:
        print("Error: Directory not found")

    except IndexError:
        print("Error: Must specify directory")

    except:
        print("Error: Directory not found")

def drive(drive_select): # Drive Selection

    if "drive" in drive_select:
        drive_select = drive_select.replace("drive ","")

    if ":" in drive_select:
        drive_select = drive_select.replace(":","")
    #print(drive_select.upper())

    try:

        f = open(root_dir+"/config/drives.ini","r")
        drives = f.readlines()
        f.close()

        loop = 0

        for i in range(len(drives)):
            if drives[loop][2] == drive_select.upper():
                drive_select = (drives[loop][0])
            loop = loop+ 1
    
    except FileNotFoundError:
        f = open(root_dir+"/config/drives.ini","w")
        drives = []
        for l in string.ascii_uppercase:
            if os.path.exists(l+":\\"):
                drives.append(l+" "+l+"\n")

        loop = 0
        for i in range(len(drives)):
            f.write(drives[loop])
            loop = loop + 1
        f.close()

    drive_select = drive_select+":\\"
    os.chdir(drive_select)
    
    #except:
        #print("Drive not found")

    com.com()

def disks():
    drives = []
    
    for l in string.ascii_uppercase:
        if os.path.exists(l+":\\"):
            drives.append(l)
    print("There are "+str(len(drives))+" hard drive(s) installed:")
    loop = 0
    loops = len(drives)
    for i in range(loops):
        print(drives[loop]+":")
        loop = loop + 1
    com.com()
  
def copy(copy_command):

    try:
        copy_str = copy_command.replace("copy ","")

        loop = 0
        spaces = []

        for i in range(len(copy_str)):
            if copy_str[loop] == " ":
                spaces.append(loop)

            loop = loop + 1
    
        loop = 0

        for i in range(len(spaces)):

            if os.path.isfile(copy_str[:spaces[loop]]) == True:
                copy_file = (copy_str[:spaces[loop]])
            
            loop = loop+1

        copy_folder = copy_str.replace(copy_file+" ", "")
        shutil.copyfile(copy_file,copy_folder+"//"+copy_file)

    except IndexError:
        print("Error: Must specify file or directory")

    except FileExistsError:
        print("Error: File already exists")

    except:
        print("Error: File or Directory not found")

    com.com()

def move(move_command):
    ensure = input("Are you sure you want to delete this file? [Y/N]: ")
    if ensure == "y" or "Y": 
        try:
            move_str = move_command.replace("move ","")

            loop = 0
            spaces = []

            for i in range(len(move_str)):
                if move_str[loop] == " ":
                    spaces.append(loop)

                loop = loop + 1
        
            loop = 0

            for i in range(len(spaces)):

                if os.path.isfile(move_str[:spaces[loop]]) == True:
                    move_file = (move_str[:spaces[loop]])
                
                loop = loop+1

            move_folder = move_str.replace(move_file+" ", "")
            shutil.copyfile(move_file,move_folder+"//"+move_file)

            os.remove(move_file)

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
        if del_command[:4] == "del ":
            del_file = del_command.replace("del ","")
        elif del_command[:6] == "delete":
            del_file = del_command.replace("delete ","")
        elif del_command[:5] == "erase":
            del_file = del_command.replace("delete ","")
        
        if os.path.isfile(del_file) == True or os.path.isdir(del_file) == True:
            ensure = input("Are you sure you want to delete this file? [Y/N]: ")
            if ensure == "y" or "Y":  
                os.remove(del_file)
        else:
            print("Error: File not found")

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
        if ren_command[:4] == "ren ":
            ren_str = ren_command.replace("ren ","")
        elif ren_command[:6] == "rename":
            ren_str = ren_command.replace("rename ","")

        loop = 0
        spaces = []

        for i in range(len(ren_str)):
            if ren_str[loop] == " ":
                spaces.append(loop)

            loop = loop + 1
    
        loop = 0

        for i in range(len(spaces)):

            if os.path.isfile(ren_str[:spaces[loop]]) == True:
                ren_file = (ren_str[:spaces[loop]])
            elif os.path.isdir(ren_str[:spaces[loop]]) == True:
                ren_file = (ren_str[:spaces[loop]])
            
            loop = loop+1

        new_name = ren_str.replace(ren_file+" ", "")
        
        if ren_file.find(".") != -1 and os.path.isfile(ren_file):
            
            ext_len = len(ren_file) - (ren_file.index("."))
            
            file_extension = "."
            ext_loop = ren_file.find(".") + 1
            for i in range(ext_len - 1):
                file_extension = file_extension + ren_file[ext_loop]
                ext_loop = ext_loop + 1
            #print(file_extension)
        
            if file_extension not in new_name:
                new_name = new_name+file_extension
        
            os.rename(ren_file,new_name)
        else:
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

def deltree(dt_command):

    try:
        ensure = input("Are you sure you want to remove this directory and its contents? [Y/N]: ")
        if ensure == "Y" or ensure == "y":
            dt_folder = dt_command.replace("deltree ", "")

            current_dir = os.getcwd()
            dt_folder = current_dir+"\\"+dt_folder

            shutil.rmtree(dt_folder)

    except:
        print("Error: File or Directory not found")

def xcopy(xc_command):
    try:
        if xc_command[:5] == "xcopy":
            xc_str = xc_command.replace("xcopy ","")
        elif xc_command[:8] == "robocopy":
            xc_str = xc_command.replace("robocopy ","")

        loop = 0
        spaces = []

        for i in range(len(xc_str)):
            if xc_str[loop] == " ":
                spaces.append(loop)

            loop = loop + 1
    
        loop = 0

        #print(spaces)
        for i in range(len(spaces)):

            if os.path.isdir(xc_str[:spaces[loop]]) == True:
                xc_dir = (xc_str[:spaces[loop]])
                #print(xc_str[:spaces[loop]])
            
            loop = loop+1

        xc_destination = xc_str.replace(xc_dir+" ", "")

        shutil.copytree(xc_dir, xc_destination)

    except:
        print("Directory not found")

def compact(comp_command):

    #try:
    if 1 + 1 == 2:
        
        if comp_command[:7] == "compact":
            comp_command = comp_command.replace("compact ","")
        elif comp_command[:6] == "expand":
            comp_command = comp_command.replace("expand ","")
        if ".zip" in comp_command:
            comp_folder = comp_command.replace(".zip","")
            with zipfile.ZipFile(comp_command, 'r') as zip_ref:
                zip_ref.extractall(comp_folder)
        else:
            if os.path.isdir(comp_command) == True:
                shutil.make_archive(comp_command, "zip", comp_command)
            elif os.path.isfile(comp_command) == True:
                current_dir = os.getcwd()
                shutil.make_archive(current_dir+"\\archive", "zip", current_dir, comp_command)
    #except:
        #print("Error: Directory or Archive not found")

def label(label_command):

    try:
        f = open(root_dir+"/config/volumes.ini","r")
        volumes = f.readlines()
        f.close()
    
    except:
        f = open(root_dir+"/config/volumes.ini","w")
        volumes = []
        for l in string.ascii_uppercase:
            if os.path.exists(l+":\\"):
                volumes.append(l+" "+l+"_DRIVE\n")

        loop = 0
        for i in range(len(volumes)):
            f.write(volumes[loop])
            loop = loop + 1
        f.close()

    drives = []
    
    for l in string.ascii_uppercase:
        if os.path.exists(l+":\\"):
            drives.append(l)
    #print(drives)

    label_str = label_command.replace("label ","")
    if str(label_str[0]).upper() in drives:
        label_drive = label_str[0].upper()
        label_text = label_str.replace(label_str[:2],"")
        label_text = label_text.upper()

        loop = 0
        for lines in volumes:
            volumes[loop] = volumes[loop].replace("\n","")
            loop = loop + 1
        loop = 0
        for i in range(len(volumes)):
            if label_drive in volumes[loop][0]:
                volumes[loop] = label_drive+" "+label_text
            loop = loop + 1

        #print(label_text)
        #print(volumes)

        loop = 0

        for lines in volumes:
            volumes[loop] = volumes[loop]+"\n"
            loop = loop + 1

        f = open(root_dir+"/config/volumes.ini","w")
        f.writelines(volumes)
        f.close()

def vol(vol_command):

    vol_command = vol_command.replace("vol ","")

    try:
        f = open(root_dir+"/config/volumes.ini","r")
        volumes = f.readlines()
        f.close()
    
    except:
        f = open(root_dir+"/config/volumes.ini","w")
        volumes = []
        for l in string.ascii_uppercase:
            if os.path.exists(l+":\\"):
                volumes.append(l+" "+l+"_DRIVE\n")

        loop = 0
        for i in range(len(volumes)):
            f.write(volumes[loop])
            loop = loop + 1
        f.close()

    loop = 0
    for lines in volumes:
        volumes[loop] = volumes[loop].replace("\n","")
        if vol_command.upper() == volumes[loop][0]:
            label_txt = volumes[loop]
            label_txt = label_txt.replace(vol_command.upper()+" ","")
            print("Drive "+vol_command.upper()+": = "+label_txt)
        loop = loop + 1

def assign(ass_command):

    ass_command = ass_command.replace("assign ","")
    if len(ass_command) == 3:

        try:
            f = open(root_dir+"/config/drives.ini","r")
            drives = f.readlines()
            f.close()
        
        except:
            f = open(root_dir+"/config/drives.ini","w")
            drives = []
            for l in string.ascii_uppercase:
                if os.path.exists(l+":\\"):
                    drives.append(l+" "+l+"\n")

            loop = 0
            for i in range(len(drives)):
                f.write(drives[loop])
                loop = loop + 1
            f.close()

        loop = 0

        old_drv = ass_command[0]
        new_drv = ass_command[2]

        for i in range(len(drives)):
            if drives[loop][2] == new_drv.upper():
                unavailable_drv = 1

        for lines in drives:
            drives[loop] = drives[loop].replace("\n","")

            if ass_command[0].upper() == drives[loop][0]:
                drives[loop] = ass_command.upper()
            loop = loop + 1
            
        f = open(root_dir+"/config/drives.ini","w")
        loop = 0
        for i in range(len(drives)):
            f.write(drives[loop].upper()+"\n")
            loop = loop + 1
        f.close()

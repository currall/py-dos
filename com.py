import os
import files
import about
import edit
import system


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
        elif command[:3] == "dir":
            files.dir(command)
            restart()

        elif command == "disks" or command == "fdisk":
            files.disks()

        elif command[:2] == "cd" or command[:5] == "chdir":
            if ".." in command:
                files.updir()
            else:
                files.cd(command)
        elif command[:2] == "md" or command[:5] == "mkdir":
            files.md(command)

        elif command[:2] == "rd" or command[:5] == "rmdir":
            files.rd(command)

        elif command[:3] == "del":
            files.delete(command)
                
        elif command[1] == ":":
            files.drive(command[0])

        elif command == "ver":
            system.ver()
            
        elif command == "about":
            about.about()
            restart()

        elif command == "clock":
            system.clock()
            
        elif command[:4] == "help":
            about.help(command)
            restart()

        elif command == "cls":
            system.cls()

        elif command[:4] == "type":
            edit.type(command)
            restart()

        elif command[:4] == "edit":
            edit.edit(command)
            restart()
            
        elif command[:3] == "ren":
            files.rename(command)

        elif command[:4] == "copy":
            files.copy(command)
        
        # error  
        elif "exe" in command:
            system.exe(command)

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

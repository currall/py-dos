import os
import files
import about
import edit
import system
import subprocess

root_dir = os.getcwd()

def restart():
    com()
    
def com(): # Command Prompt

    os.system("color")

    #try:
    if 1 == 1:

        # GETTING PROMPT TEXT
        
        current_dir = os.getcwd()

        if os.path.isfile(root_dir+"/config/system.ini") == False:
            exit()

        with open(root_dir+"/config/system.ini","r") as f:
            system_ini = f.readlines()
            prompts = []
            loop = 0
            
            for i in range(len(system_ini)):
                if "prompt" in system_ini[loop]:
                    prompts.append(system_ini[loop])
                loop = loop+ 1
            loop = 0
            for lines in prompts:
                prompts[loop] = prompts[loop].replace("prompt ","")
                prompts[loop] = prompts[loop].replace("\n","")
                loop = loop + 1
            if prompts[0] == "0":
                prompt = current_dir+"> "
                prompt = prompt.upper()
            else:
                prompt = prompts[1]
                prompt = prompt.upper()
        
        command = input(prompt)
        command = command.casefold()
        #boot
        if command == "command":
            restart()
        
        # FILE BROWSING AND MANAGEMENT
        
        elif command[:3] == "dir":
            files.dir(command)
            restart()

        elif command[:4] == "find":
            files.find(command)
            restart()

        elif command == "disks":
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

        elif command[:4] == "del " or command[:6] == "delete" or command[:5] == "erase":
            files.delete(command)
                
        elif command[1] == ":" or command[:5] == "drive":
            files.drive(command)

        elif command[:3] == "ren" or command[:6] == "rename":
            files.rename(command)
            restart()

        elif command[:4] == "copy":
            files.copy(command)
            restart()

        elif command[:4] == "move":
            files.move(command)
            restart()

        # ADVANCED FILE MANAGEMENT

        elif command[:7] == "fdisk":
            files.fdisk(command)
            restart()

        elif command[:4] == "2bin":
            files.file2bin(command)
            restart()

        elif command[:4] == "comp":
            files.comp(command)
            restart()

        elif command[:7] == "deltree":
            files.deltree(command)
            restart()

        elif command[:5] == "xcopy" or command[:8] == "robocopy":
            files.xcopy(command)
            restart()

        elif command[:7] == "compact" or command[:6] == "expand":
            files.compact(command)
            restart()

        elif command[:5] == "label":
            files.label(command)
            restart()

        elif command[:3] == "vol":
            files.vol(command)
            restart()
        
        elif command[:6] == "assign":
            files.assign(command)
            restart()

        # SETTINGS

        elif command[:5] == "color":
            system.color(command)
            restart()
        
        elif command[:5] == "uname" or command[:8] == "username":
            system.username(command)
            restart()

        elif command == "ver":
            system.ver()
            restart()

        elif command == "oldver":
            system.oldver()
            restart()

        elif command[:6] == "setver":
            system.setver(command)
            restart()

        

        # HELP AND ABOUT
        
        elif command == "about":
            about.about()
            restart()
        
        elif command == "intro":
            about.intro()
            restart()

        elif command[:4] == "help" or command[-4:] == "help":
            about.help(command)
            restart()

        # CLOCK, DATE AND TIME
    
        elif command == "clock":
            system.clock("c")
            restart()
        elif command == "date":
            system.clock("d")
            restart()
        elif command == "time":
            system.clock("t")
            restart()
            
        elif command == "cls":
            system.cls()
            restart()

        # TEXT FILE MANAGEMENT

        elif command[:4] == "type":
            edit.type(command)
            restart()

        elif command[:4] == "edit":
            edit.edit(command)
            restart()

        elif command[:5] == "edlin":
            edit.edlin(command)
            restart()

        # PROMPT

        elif command == "pause":
            print("Press Enter to continue.")
            input()
            restart()

        elif command[:4] == "echo":
            system.echo(command)
            restart()

        elif command[:3] == "rem":
            restart()

        elif command[:6] == "prompt":
            system.prompt(command)
            restart()
            
        # EXECUTABLES
         
        elif command[:3] == "exe" or command[-3:] == "exe":
            system.exe(command)
            restart()
        
        elif command[:3] == "cmd":
            system.cmd(command)
            restart()
        
        elif command[:2] == "py" or command[-2:] == "py":
            system.py(command)
            restart()

        # SYSTEM COMMANDS

        elif command[:5] == "clip ":
            system.clip(command)
            restart()
        elif command == "paste":
            system.paste()
            restart()
        elif command[:8] == "shutdown":
            system.shutdown(command)
            restart()

        elif command == "exit":
            exit_q = input("Are you sure you want to exit DOS? [Y/N]: ")
            if exit_q == "y" or exit_q == "Y":
                exit()
            else:
                restart()
        
        elif command == "break":
            exit()
        
        else:

            # WINDOWS EXECUTABLES WITHOUT EXE COMMAND
            
            if os.path.isfile(command+".exe") == True:
                subprocess.Popen(command+".exe")
                restart()

            elif os.path.isfile(command+".py") == True:
                os.sytem("py "+command+".py")
                restart()

            # UNKNOWN COMMAND
            
            else:
                print("Error: Command not found")
                restart()
'''
    except SystemExit:
        exit()
    
    except:
        print("Error: Command not found")
        restart()
'''


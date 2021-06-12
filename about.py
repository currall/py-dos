# HELP SCRIPT v3

import os

root_dir = os.getcwd()

def about():
    os.system("cls")
    
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

    boot_string = (" PY-DOS Command Prompt "+str(ver))

    boot_equals = "="
    for i in range(len(boot_string)):
        boot_equals = boot_equals+"="
    
    print(boot_equals)
    print(boot_string)
    print(boot_equals)

    print("")
    h=open(root_dir+"/help/help.txt","r")
    help_lines = h.read().splitlines()

    help_total = 9
    loop = 0
    for i in range(help_total):
        print(help_lines[loop])
        loop = loop + 1

def help(help_command):

    tre_line = 0

    

    # GENERIC HELP DIALOGUES

    if "help all" in help_command or "doshelp" in help_command:
        help_start = 94
        h=open(root_dir+"/help/help.txt","r")
        help_length = h.readlines()
        help_end = len(help_length)
        not_help = 0
        tre_line = 1
    elif help_command == "help" or help_command == "fasthelp":
        help_start = 10
        help_end = 23
        not_help = 0
    elif help_command == "oldhelp":
        help_start = 24
        help_end = 93
        not_help = 0

    # HELP COMMANDS

    else:
        loop = 0

        h=open(root_dir+"/help/commands.txt","r")
        commands = h.read().splitlines()

        help_command2 = help_command.replace("help ","")
        help_str = "HELP - " + help_command2.upper()


        while commands[loop] != help_str:
            loop = loop + 1
        help_start = loop

        loop = loop + 1

        while not "HELP - " in commands[loop]:
            if not loop >= len(commands):
                loop = loop + 1
        
        help_end = loop

        not_help = 1

    # INTERPRETATION

    if not_help == 0:
        h=open(root_dir+"/help/help.txt","r")
        help_lines = h.read().splitlines()
    elif not_help == 1:
        h=open(root_dir+"/help/commands.txt","r")
        help_lines = h.read().splitlines()
    

    # PRINTING

    if tre_line != 1:  
        help_total = help_end - help_start
        loop = help_start
        for i in range(help_total):
            print(help_lines[loop])
            loop = loop + 1

    elif tre_line == 1:
        print("=======")
        print("DOSHELP")
        print("=======")
        print("")

        help_total = help_end - help_start
        loop = help_start

        help_total = help_end - help_start
        if help_total % 3 != 0:
            help_total2 = (help_total // 3) + 1
        else:
            help_total2 = (help_total // 3)

        loop = help_start

        help_lines2 = []

        for i in range(help_total):
            help_lines2.append(help_lines[loop])
            loop = loop + 1
        
        help_lines2 = sorted(help_lines2)

        loop = 0

        for i in range(help_total2):
            try:
                space1loop = 15 - len(help_lines2[loop])
                space2loop = 15 - len(help_lines2[loop + 1])
                space1 = ""
                space2 = ""
                for i in range(space1loop):
                    space1 = space1 + " "
                for i in range(space2loop):
                    space2 = space2 + " "
                print(help_lines2[loop] + space1 + help_lines2[loop + 1] + space2 + help_lines2[loop + 2])
            except IndexError:
                try:
                    print(help_lines2[loop] + space1 + help_lines2[loop + 1])
                except IndexError:
                    print(help_lines2[loop])
            loop = loop + 3

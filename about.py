import os

def about():
    print("")
    h=open("help//help.txt","r")
    help_lines = h.read().splitlines()

    help_total = 9
    help_loop = 0
    for i in range(help_total):
        print(help_lines[help_loop])
        help_loop = help_loop + 1

def help(help_command):

    if "exe" in help_command:
        help_start = 0
        help_end = 10
        not_help = 1
    elif "dir" in help_command:
        help_start = 11
        help_end = 21
        not_help = 1
    elif "cd" in help_command:
        help_start = 22
        help_end = 29
        not_help = 1
    elif "md" in help_command:
        help_start = 30
        help_end = 37
        not_help = 1
    elif "rd" in help_command:
        help_start = 38
        help_end = 45
        not_help = 1
    elif "del" in help_command:
        help_start = 46
        help_end = 53
        not_help = 1
    elif "ren" in help_command:
        help_start = 54
        help_end = 61
        not_help = 1
    elif "drive" in help_command:
        help_start = 62
        help_end = 69
        not_help = 1
    elif "disks" in help_command:
        help_start = 70
        help_end = 75
        not_help = 1
    elif "ver" in help_command:
        help_start = 76
        help_end = 79
        not_help = 1
    elif "type" in help_command:
        help_start = 80
        help_end = 88
        not_help = 1
    elif "edit" in help_command:
        help_start = 89
        help_end = 100
        not_help = 1
    elif "help help" in help_command:
        help_start = 101
        help_end = 108
        not_help = 1
    elif "copy" in help_command:
        help_start = 109
        help_end = 116
        not_help = 1
    elif "move" in help_command:
        help_start = 117
        help_end = 124
        not_help = 1
    elif "clock" in help_command:
        help_start = 125
        help_end = 128
        not_help = 1
    else:
        help_start = 11
        h=open("help//help.txt","r")
        help_length = h.readlines()
        help_end = len(help_length)
        not_help = 0

    if not_help == 0:
        h=open("help//help.txt","r")
        help_lines = h.read().splitlines()
    elif not_help == 1:
        h=open("help//commands.txt","r")
        help_lines = h.read().splitlines()
        
    help_total = help_end - help_start
    help_loop = help_start
    for i in range(help_total):
        print(help_lines[help_loop])
        help_loop = help_loop + 1   
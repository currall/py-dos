import os

def type(type_command):
    #print(type_command)

    try:
        type_char = int(len(type_command)-6)
        #print(make_dir_char)
        type_loop = 5
        type_file = type_command[5]
        for i in range(type_char):
            type_loop = type_loop + 1
            type_file = type_file + type_command[type_loop]

        if ".txt" not in type_file:
            type_file = type_file+".txt"

        f = open(type_file)
        print(f.read())
        f.close()
        
    except FileNotFoundError:
        print("Error: File not found")

    except IndexError:
        print("Error: Must specify file")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: File not found")

def edit(edit_command):
    #print(edit_command)
    try:
        edit_char = int(len(edit_command)-6)
        #print(make_dir_char)
        edit_loop = 5
        edit_file = edit_command[5]
        for i in range(edit_char):
            edit_loop = edit_loop + 1
            edit_file = edit_file + edit_command[edit_loop]

        if ".txt" not in edit_file:
            edit_file = edit_file+".txt"
            
        f = open(edit_file)
        edit_array = f.read().splitlines()
        edit_len = len(open(edit_file).readlines(  ))
        edit_loop = 0
        for i in range(edit_len):
            print(str(edit_loop + 1)+": "+edit_array[edit_loop])
            edit_loop = edit_loop + 1
        f.close()

        
        edit_line = int(input("Enter Line no. to edit: "))
        f = open(edit_file,"r")
        edited = f.readlines()
        edit_content = input("What to replace line "+str(edit_line)+" with: ")
        edit_content = edit_content + "\n"
        #print(edit_line)
        #print(len(edited))
        if edit_line > (len(edited)):
            f.close()
            for i in range(edit_line - len(edited)):
                edited.append("\n")
        
        f.close()
        with open(edit_file,"w") as f:
            edited[edit_line - 1] = edit_content
            f.writelines(edited)
        
    except FileNotFoundError:
        print("Error: File not found")

    except IndexError:
        f = open("NEW DOC.TXT","w")
        print("Created 'NEW DOC.TXT'. Run 'EDIT' again to modify this file")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: File not found")

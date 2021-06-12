import os
import com

root_dir = os.getcwd()

def type(type_command):
    #print(type_command)

    try:
        type_file = type_command.replace("type ","")

        if "." not in type_file:
            type_file = type_file+".txt"

        f = open(type_file)
        print(f.read())
        f.close()
        
    except FileNotFoundError:
        f = open(type_file,"a")
        f.close()
        print("File Created. Run the 'EDIT' command to edit")

    except IndexError:
        print("Error: Must specify file")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: File not found")

def edit(edit_command):
    #print (edit_command)
     
    os.system("cls")
    os.system("color 17")

    try:
        if "edit " in edit_command:
            edit_file = edit_command.replace("edit ","")
        elif "edlin " in edit_command:
            edit_file = edit_command.replace("edlin ","")

        if "." not in edit_file:
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
        f = open(edit_file,"a")
        f.close()
        print("File Created. Run this command again to edit")

    except IndexError:
        f = open("NEW DOC.TXT","w")
        print("Created 'NEW DOC.TXT'. Run 'EDIT' again to modify this file")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: File not found")
    
    os.system("cls")

def edlin(edit_command):
    #print(edit_command)
    try:
        if "edit " in edit_command:
            edit_file = edit_command.replace("edit ","")
        elif "edlin " in edit_command:
            edit_file = edit_command.replace("edlin ","")

        if "." not in edit_file:
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
        f = open(edit_file,"a")
        f.close()
        print("File Created. Run this command again to edit")

    except IndexError:
        f = open("NEW DOC.TXT","w")
        print("Created 'NEW DOC.TXT'. Run 'EDIT' again to modify this file")

    except OSError:
        print("Error: The syntax of the command is incorrect")

    except:
        print("Error: File not found")

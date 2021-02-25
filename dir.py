import os

def dir(dir_command):
    
    temp_dir = os.getcwd()
    files = os.listdir(temp_dir)
    
    if("/w" in dir_command):
        print(files)
    elif("/s" in dir_command):
        dir_command.index("/")
        if int(dir_command.index("/")) == int(dir_command.index("s")-1):
            searched_dir = []
            #print("ok")
            dir_search_len = len(dir_command) - int(dir_command.index("s")+2)
            #print(len(dir_command))
            #print(dir_search_len)
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

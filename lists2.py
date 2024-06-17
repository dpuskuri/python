import os

folders = input("please provide list of folder names with spaces in between:").split()
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError: 
        print("plese provide the right folder name, looks like this folder dose not exist" + folder)
        break
    except PermissionError:
        print("no access to this folder" + folder)
    print("listing file names for the folder -" + folder)
    except 
    
    for file in files:
        print(file)


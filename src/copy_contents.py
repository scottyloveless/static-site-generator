import os, shutil

def copy_static_to_public(current_path="static", destination="public"):
    if current_path == "static":
        if os.path.exists("public"):
            shutil.rmtree("public")
            print("public removed")
            os.mkdir("public")
            print("public created")
    
    dir_list = os.listdir(current_path)
    #base case == if node is file and not folder
    for item in dir_list:
        if item == ".DS_Store":
            pass
        new_current_path = os.path.join(current_path, item)
        new_destination_path = os.path.join(destination, item)
        if os.path.isfile(new_current_path):
            #copy single file
            shutil.copy(new_current_path, new_destination_path)
        else:
            #make directory with same name
            os.mkdir(new_destination_path)
            #keep going to next
            copy_static_to_public(new_current_path, new_destination_path)


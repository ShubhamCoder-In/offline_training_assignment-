import os
import shutil
print("welcome to filter file with catagories it support pdf, jpg, png, pptx, jpeg, txt file ......")
directory_input = input("enetr your file directory with adsuloute path:")
input_check = os.path.exists(directory_input)
if input_check :
    file_dir = (directory_input)
    os.chdir(file_dir)
    list = os.listdir()
    # print(list)
    file_name = []
    extense = []
    # store extensen to detect file directory
    pdf = []
    jpg = []
    jpeg = []
    png = []
    txt = []
    ppt = []
    # get file extense and put in file folder
    for key, data in enumerate(list) :
        name, ext = os.path.splitext(data)
        file_name.append(name) 
        extense.append(ext)
        if extense[key] == ".jpg" :
            jpg.append(data)
        if extense[key] == ".png" :
            png.append(data)
        if extense[key] == ".jpeg" :
            jpeg.append(data)
        if extense[key] == ".pdf" :
            pdf.append(data)
        if extense[key] == ".txt" :
            txt.append(data)
        if extense[key] == ".pptx" :
            ppt.append(data)

    folder_format = ["pdf","jpg","jpeg","txt","png","ppt"]
    file_ext = [pdf,jpg,jpeg,txt,png,ppt]
    for i, value in enumerate(folder_format):
        new_path = os.path.join(file_dir,value)
        if not os.path.exists(new_path) and len(file_ext[i])!=0:
            os.makedirs(new_path)
        for value in file_ext[i]: 
            current_path = os.path.join(file_dir,value)
            new_file_path = os.path.join(new_path,value)
            print( current_path," -- : ---", new_file_path)
            if not os.path.exists(new_file_path):
                shutil.move(current_path , new_file_path)
else:
    print("please enter absuloute file path in system not find vaild path")
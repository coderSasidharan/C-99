import os
import shutil

path = "C:/Users/Vaidya/Desktop/Code/C-99"
listoffiles = os.listdir(path)

for file in listoffiles:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.copy(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.copy(path+'/'+file,path+'/'+ext+'/'+file)

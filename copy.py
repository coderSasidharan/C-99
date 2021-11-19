import os
import shutil

path = "C:/Users/Vaidya/Desktop/Code/C-99"
print("before copying file")
print(os.listdir(path))

source = 'C:/Users/Vaidya/Desktop/Code/C-99/info.txt'
destination = 'C:/Users/Vaidya/Desktop/Code/C-99/info2.txt'
dest = shutil.copy(source, destination)

print("after copying file")
print(os.listdir(path))
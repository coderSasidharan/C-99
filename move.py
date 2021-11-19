import os
import shutil

path = "C:/Users/Vaidya/Desktop/Code/C-99"
print("before copying file")
print(os.listdir(path))

source = 'C:/Users/Vaidya/Desktop/Code/C-99/info3.txt'
destination = 'C:/Users/Vaidya/Desktop/Code/C-99/sasi/info3.txt'
dest = shutil.move(source, destination)

print("After copying file")
print(os.listdir(path))
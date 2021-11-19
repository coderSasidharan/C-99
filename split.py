import os
path = "C:/Users/Vaidya/Desktop/Code/C-99/info.txt"
routeExtension = os.path.splitext(path)

print("root part ", routeExtension[0])
print("extension part", routeExtension[1])

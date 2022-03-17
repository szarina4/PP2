import os
def access(path):
    if os.access(path, os.F_OK) and  os.access(path, os.R_OK) and  os.access(path, os.W_OK) and  os.access(path, os.X_OK) :
        return True
    return False

path1=input("Enter path")
if os.path.exists(path1):
    if access(path1):
        os.remove(path1)
        print("success!")
    else:
        print("Not accesible")
else:
    print("no such path")   

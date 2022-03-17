import os
path=input()
if os.path.exists(path):
    print("File name:",os.path.basename(path))
    print("Directory name:",os.path.dirname(path))
else:
    print("no such path exists ")
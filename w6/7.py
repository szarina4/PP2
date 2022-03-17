import os
import shutil
file_name=input("Enter the file you want to copy: ")
copied=input("Enter to where to copy?")
shutil.copy(file_name,copied)

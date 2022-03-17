import os
print('Exist:', os.access(r'C:\Users\bolat\Documents\PP2\PP2\w6', os.F_OK))
print('Readable:', os.access(r'C:\Users\bolat\Documents\PP2\PP2\w6', os.R_OK))
print('Writable:', os.access(r'C:\Users\bolat\Documents\PP2\PP2\w6', os.W_OK))
print('Executable:', os.access(r'C:\Users\bolat\Documents\PP2\PP2\w6', os.X_OK))
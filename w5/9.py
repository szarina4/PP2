import re
line = input()
x = re.finditer('[A-Z][^A-Z]*',line)
for i in x:
    print(i.group(),end=" ")
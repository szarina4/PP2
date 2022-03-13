import re
line = input()
x = re.findall('[A-Z][^A-Z]*',line)
print(x)
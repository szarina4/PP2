import re
line = input()
x = re.findall('[A-Z][a-z]+',line)
for i in x:
    print(i)
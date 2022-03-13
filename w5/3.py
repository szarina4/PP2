import re
line = input()
x = re.findall('[a-z]+_[a-z]+',line)
for i in x:
    print(i)
import re
line = input()
x = re.search('[a-z]+',line)
y=re.findall('[A-Z][a-z]+',line)
for i in range(len(y)):
    y[i] = y[i].lower()
print(x.group(),end="_")
print(*y,sep='_')
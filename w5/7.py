import re
line = input()
x=re.split('_',line)
for i in range(1,len(x)):
    x[i]=x[i].capitalize()

st=''.join(x)
print(st)

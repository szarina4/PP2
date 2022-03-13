import re
line = input()
x = re.sub('[,. ]',':',line)
print(x)
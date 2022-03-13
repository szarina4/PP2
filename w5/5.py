import re
line = input()
x = re.search('a.+b$',line)
if x:
    print('There\'s a match')
else:
    print('No match')
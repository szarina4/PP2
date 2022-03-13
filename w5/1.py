import re
line = input()
x = re.search('ab*',line)
if x:
    print('There\'s a match')
else:
    print('No match')
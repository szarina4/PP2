import re
line = input()
x = re.search('ab{2,3}',line)
if x:
    print('There\'s a match')
else:
    print('No match')
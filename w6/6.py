import string
for c in string.ascii_uppercase:
    with open(c+".txt",'x') as f:
        f.write(c)



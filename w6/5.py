a=input().split()
with open ("textfor5.txt","w") as f:
    for i in a:
        f.write("%s\n" % i)

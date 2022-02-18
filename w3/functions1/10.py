def unique(a):
    b=[]
    for x in a:
        if x not in b:
            b.append(x)
    return b

a=input().split()
print(unique(a))
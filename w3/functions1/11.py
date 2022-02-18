def ispalin(a):
    for i in range(len(a)):
        if a[i]!=a[len(a)-1-i]:
            return False
    return True

line=input()
print(ispalin(line))
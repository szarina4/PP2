line=input()
a=[]
def check(line):
    for i in range(len(line)):
        if line[i]=='(' or line[i]=='{' or line[i]=='[':
            a.append(line[i])
        else:
            if(len(a)==0):
                return False
            last_added=a[len(a)-1]
            if (last_added=='[' and line[i]!=']'):
                return False
            if (last_added=='{' and line[i]!='}'):
                return False
            if (last_added=='(' and line[i]!=')'):
                return False
            a.pop(-1)
    return True
if(check(line)==True):
    if(len(a)==0):
        print("Yes")
    else:
        print("No")
else:
    print("No")



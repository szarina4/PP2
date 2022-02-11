def fucn(line):
    if(ord(line)>=65 and ord(line)<=90):
        return True
    if(ord(line)>=97 and ord(line)<=122):
        return True
    return False
    


s=input()
for i in s:
    if  fucn(i):
        continue
    else:
       s=s.replace(i," ")       
a=s.split() 
b=set(a)
a=list(b)
a.sort()
print(len(a)) 
for x in a:
    print(x)

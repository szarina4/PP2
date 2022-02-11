
def strong(line):
    cntlow=0
    cntbig=0
    cntnum=0
    for x in line:
       if  x.islower():
           cntlow+=1
       if  x.isupper():
            cntbig+=1
       if  x.isdigit():
            cntnum+=1
    z=cntlow*cntbig*cntnum
    return z
        

n=int(input())
a=[]
for i in range (n):
    name=input()
    a.append(name)
b=set()

for x in a:
     if (strong(x))!=0 :
        b.add(x)
    
b=list(b)
b.sort()
print(len(b))
[print(i) for i in b]




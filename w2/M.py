a=[]
while True:
    lis=list(input().split())
    if lis[0]=='0':
        break
    a.append(lis)

a=sorted(a,key=lambda x:int(x[0]))
a=sorted(a,key=lambda x:int(x[1]))
a=sorted(a,key=lambda x:int(x[2]))

for i in a:
    print(i[0],i[1],i[2])


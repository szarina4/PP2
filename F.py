n=int(input())
a=dict()
#cчитываем инпут
for i in range (n):
    name, v=map(str,input().split())
    val=int(v)
    if name in a:
       a[name]+=val
    else:
        a[name]=val
#находим макс 
b=[]
for x in a.values():
    b.append(x)

max=b[0]
for i in b:
    if max < i:
        max=i
#сортируем по key
sorteddic=sorted(a.items())
for k,v in sorteddic:
    if (max-v!=0):
        print(k,"has to receive",max-v,"tenge")
    else:
        print(k,"is lucky!")
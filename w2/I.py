n=int(input())
lst=[]
taken=[]
for i in range(n):
    a=input().split()
    op = a[0]
    if op=="1":
        name =a[1]
        lst.append(name)
    if op=="2":
        taken.append(lst[0])
        lst.pop(0)  
for i in taken:
    print(i,end=" ")
        



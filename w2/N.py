a=[]
while True:
    n=int(input())
    if(n==0):
        break
    a.append(n)

for i in range (len(a)//2):
    print(a[i]+a[len(a)-1-i],end=" ")
    
if(len(a)%2==1):
    print(a[len(a)//2])
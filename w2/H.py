import math
x,y=map(int,input().split())
def func(kk):
    a,b=kk[0],kk[1]
    dis=math.sqrt((a-x)**2+(b-y)**2)
    return dis
n=int(input())
arr=[]
#лист в листе
for i in range(n):
    list=input().split()
    list=[int(x) for x in list]
    arr.append(list)
    list=[]
arr.sort(key=func)
for x in arr:
    print(x[0], x[1])
n=int(input())
def gen(n):
    for i in range (n):
        if i%2==0:
            yield i
a=gen(n)  
print(*a,sep=",")
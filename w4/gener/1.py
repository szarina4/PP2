n=int(input())
def gen(n):
    for i in range (n):
        yield i*i
   
for k in gen(n):
    print(k,end=" ")
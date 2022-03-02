a,b=int(input()),int(input())
def squares(a,b):
    for i in range (a,b,):
        yield i*i
   
for k in squares(a,b):
    print(k,end=" ")
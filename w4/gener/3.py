n=int(input())
def gen(n):
    for i in range (n):
        if i%3==0 and i%4==0:
            yield i
print(list(gen(n)))

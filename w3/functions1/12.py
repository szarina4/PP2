def histogram(a):
    for x in a:
        print('*'*x)

a=list(map(int,input().split()))
histogram(a)
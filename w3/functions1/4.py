def isprime(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
         if (x % i) == 0:
            return False
        return True
    else:
        return False

def filter_prime(a):
    b=[]
    for x in a:
        if isprime(x):
            b.append(x)
    return b

a=list(map(int,input().split()))
print(filter_prime(a))


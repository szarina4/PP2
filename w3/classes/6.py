def isprime(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
         if (x % i) == 0:
            return False
        return True
    else:
        return False

arr=list(map(int,input().split()))
newarr=list(filter(lambda x: isprime(x),arr))
print(newarr)
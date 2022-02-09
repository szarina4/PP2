def isPrime (num):
    if num==1 :
        return False
    for i in range (2,num,1):
        if num%i==0:
            return False
    return True

a,c=map(int, input().split())
ok=False
if (a<=500):
    if(isPrime(a)):
        if(c%2==0):
            ok=True
if ok:
    print("Good job!")
else:
    print("Try next time!")


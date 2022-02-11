n=int(input())
a = [int(x) for x in input().split()]

b=a.copy()
max=a[0]*a[1]
for i in range (len(a)):
    for j in range (len(b)):
        if(i==j):
            continue
        if (a[i]*b[j] > max):
            max=a[i]*b[j]
print(max)


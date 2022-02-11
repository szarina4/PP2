a = [int(x) for x in input().split()]
b=[0]*len(a)
b[0]=1

def steps(ind,step):
    for i in range (0,step+1,1):
        if ind+i>=0 and i+ind<len(a) and b[ind]!=0:
            b[ind+i]=1

for ind,val in enumerate(a):
    steps(ind,val)

print(b[len(b)-1])

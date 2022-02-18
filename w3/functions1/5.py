from itertools import permutations
s=set()
def allperm():
    line=input()
    for i in(permutations(line)):
        s.add(i)
    b=list(s)
    for x in b:
        print(x)
#сет для того чтобы не было одинаковых перм
allperm()
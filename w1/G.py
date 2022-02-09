line=input()
j=len(line)-1
i=0
def tosum(line,i,j):
    if i==len(line):
        return 0
    x=ord(line[i])-48
    return x*(2**j)+tosum(line,i+1,j-1)
     
print(tosum(line,i,j))


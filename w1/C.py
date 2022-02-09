def  toLowercase(line):
    for i in line:
        x=ord(i)
        if x >=65 and x<=90:
            x+=32
            
        i=chr(x)
        print(i,end="")

line1=input()
toLowercase(line1)


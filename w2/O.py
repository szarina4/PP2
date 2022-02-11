s=input()
def tonum(line):
    expon=(len(line)/3)-1
    num=0
    for i in range(0,len(line),3):
        if line[i:i+3]=="ONE":
            num+=1*(10**expon)
            expon-=1
        if line[i:i+3]=="TWO":
            num+=2*(10**expon)
            expon-=1
        if line[i:i+3]=="THR":
            num+=3*(10**expon)
            expon-=1
        if line[i:i+3]=="FOU":
            num+=4*(10**expon)
            expon-=1
        if line[i:i+3]=="FIV":
            num+=5*(10**expon)
            expon-=1
        if line[i:i+3]=="SIX":
            num+=6*(10**expon)
            expon-=1
        if line[i:i+3]=="SEV":
            num+=7*(10**expon)
            expon-=1
        if line[i:i+3]=="EIG":
            num+=8*(10**expon)
            expon-=1
        if line[i:i+3]=="NIN":
            num+=9*(10**expon)
            expon-=1
        if line[i:i+3]=="ZER":
            num+=0*(10**expon)
            expon-=1
    num=int(num)    
    return num
def tostr(num):
    num=str(num)
    s=""
    for x in num:
        if x=="0":
            s+="ZER"
        if x=="1":
            s+="ONE"
        if x=="2":
            s+="TWO"
        if x=="3":
            s+="THR"
        if x=="4":
            s+="FOU"
        if x=="5":
            s+="FIV"
        if x=="6":
            s+="SIX"
        if x=="7":
            s+="SEV"
        if x=="8":
            s+="EIG"
        if x=="9":
            s+="NIN"
    return s 
s=s.replace("+"," ")
a=s.split()

"""print(a)
print(tonum(a[0]))
print(tonum(a[1]))"""


sum=tonum(a[0])+tonum(a[1])
print(tostr(sum))

        
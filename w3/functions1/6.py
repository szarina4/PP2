def rever():
    line = input()
    b = ''
    a = line.split()
    for i in range(len(a)):
        b = a[i] +' ' + b
    
    return b 

print(rever())

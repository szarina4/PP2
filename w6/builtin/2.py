line=input("Input your string: ")
up_count=0
low_count=0
for i in line:
    if i.isupper():
        up_count+=1
    if i.islower():
        low_count+=1

print("Numebr of upper case letters is",up_count)
print("Numebr of lower case letters is",low_count)
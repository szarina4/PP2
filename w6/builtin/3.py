x=input("Enter yout string: ")
y=''.join(reversed(x))
if y==x:
    print("The palindrome!")
else:
    print("No")

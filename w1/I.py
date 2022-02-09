num=int(input())
st="@gmail.com"
for i in range(num):
    line=input()
    if st in line:
        line=line.strip("@gmail.com")
        print(line)
            
#тут проверяю верт.или гор.
nums = input().split()
if len(nums) > 1:
  n, x = map(int, nums)
else:
  n = int(nums[0])
  x = int(input())

if (n==1):
    print(x)
else:
    arr=[]
    for i in range(n):
        j=x+2*i
        arr.append(j)
    xor=arr[0]
    for i in range(1,n):
        xor^=arr[i]
    print(xor)



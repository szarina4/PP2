def has_33(nums):
    for i in range (len(nums)):
        if i+1>=0 and i+1<len(nums):
            if(nums[i]==3 and nums[i+1]==3):
                return True
    return False

a=list(map(int,input().split()))
if has_33(a):
    print("Has 2 consecutive three's")
else:
    print("Doesnt have 2 consectutive three's")

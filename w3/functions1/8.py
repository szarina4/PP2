def spy_game(nums):
    if 0 not in nums:
        return False
    if 7 not in nums:
        return False
    for i in range(len(nums)):
        if nums[i]==0:
            for j in range(i+1,len(nums)):
                if nums[j]==0:
                    for k in range(i+2,len(nums)):
                        if nums[k]==7:
                            return True
    return False

nums=list(map(int,input().split()))
print(spy_game(nums))
        
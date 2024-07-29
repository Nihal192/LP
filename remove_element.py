j=0     #this will be final o/p

for i in range(len(nums)):
    if nums[i]!=val:
        nums[j]=nums[i]
        j+=1
    return j
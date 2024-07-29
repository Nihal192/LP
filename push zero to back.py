# intialize two pointer L,R and set values
l=len(nums)
r=0
for i in range(l):   #make sure you run the loop in the 'l' and not in 'Len(nums)'
    if nums[i]!=0:
        nums[l],nums[r] = nums[r],num[l]   #basic swapping
        r+=1



        
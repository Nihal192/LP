#logic is simple if the sum>target inc left by1 if not incerement Right by 1 and when l==r then return the index of both l,r . 
#here will add 1 to index as it starts from 1 given in question

l,r=0,len(nums)-1
while l<r:
  cs=num[l]+num[r]
  if cs>nums:
    r-=1
  elif cs<nums:
    l+=1
  else:
    return(l+1,r+1)
return[]

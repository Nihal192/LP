window= set()
l=0
for r in range(len(nums)):
  if r-l>k:
    window.remove(nums[l])
    l+=1
  if nums[r] in window:
  return true
windows.add(nums[r])
return false 

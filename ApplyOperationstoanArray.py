class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

      l=0
      for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
          nums[i]*=2
          nums[i+1]=0
      for i in range(len(nums)):
        if nums[i]:
          nums[l],nums[i] = nums[l],nums[i]
          l+=1
    return nums

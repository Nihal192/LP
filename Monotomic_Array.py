class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
      increase,decrease=True,True
      for i in range(len(nums)-1):
        if not (nums[i]<=nums[i+1]):
          increment=False
        if not (nums[i]>=nums[i+1]):
          decrease=True
      return increase or decrease

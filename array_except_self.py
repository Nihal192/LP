
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       res=[1]*(len(nums))
       prefix=1
       for i in range(len(nums)):
         res[i]=prefix
         postfix*=nums[i]
       Postfix=1
       for i in range(len(nums)-1,-1,-1):
         res[i] *=postfix
         postifx*=nums[i]
         return(res)
              

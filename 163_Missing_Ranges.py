class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:  #ahiya apde check karisu ke nums na hoi toh su karvanu.
         return[[lower,upper]]
        res=[]  #it will store result over iteration and will return at end
        if nums[0]!=lower:  #jo nums no pelo number and lower same na hoi to 1st lower  and nums[0]-1
         res.append([lower,nums[0]-1])
        for i in range(len(nums)-1):
         if nums[i+1] - nums[i] > 1:
          res.append([nums[i]+1 , nums[i+1]-1])
        if nums[-1]!=upper:  #jo nums last number and upper same na hoi to 1st num +1 and upper as it is
         res.append([nums[-1] +1,upper])
        return res 

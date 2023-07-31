class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c,r=0,0   #c is for count and res is result
        for n in nums:  #scanning every element
            if c==0:    #if count is zero then push the encountered number into result
                r=n
            c+=(1 if n==r else -1)  #check if encountered num is ==result then  inc count by 1 else count dec 1
        return(r)  #return result
        

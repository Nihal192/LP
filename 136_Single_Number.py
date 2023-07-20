class Solution:
    def singleNumber(self, nums):
        result = 0 #varibale jema apde result of xor store kari daisu
        for num in nums:  #darek value scan karisu in nums
            result =num^result  #ape num ne xor karaisu result jode 
        return result

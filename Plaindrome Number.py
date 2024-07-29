#Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        number=x
        rnum=0
        while number:
            rnum = rnum * 10 + number % 10
            number = number // 10
        return x == rnum

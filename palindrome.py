class Solution:
    def isPalindrome(self, s: str) -> bool:

      #TWO POINTER I ND J , THAT GOES FROM START TO END
      i=0
      j= len(nums)-1
      while i < j :
          while i < j and not s[i].isalnum():
            i+=1
          while i < j and not s[j].isalnum():
            j-=1

          if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1
     return False      

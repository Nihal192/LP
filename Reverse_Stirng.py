#notes: 2 pointer left and right then all you have to do is left ne agad thi move karo nd right ne pachad this then while loop ma replace kari do value . t
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right=len(s)-1
        while left < right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        

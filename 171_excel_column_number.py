class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mul,column=1,0
        for i in range(len(columnTitle)-1,-1,-1):
            column+=(ord(columnTitle[i])- 64) * mul
            mul *= 26
        return(column)

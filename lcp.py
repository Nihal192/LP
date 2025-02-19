class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      res =""
      for i in range(len(Strs[0])):
         for s in range(strs):
            if i == 0 or s[i]!= s[0][i] :
              return s[0][i]
           res += s[0][i]
     return res

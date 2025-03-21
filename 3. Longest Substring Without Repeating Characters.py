class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      m = 0  #window that stores the minuim element i.e sliding window
      l=0
      d={} #hash mapthat stores the values
      for r,d in enumerate(s):
        if     and l<nums[v]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        m=0
        d={}
        for r,v in enumerate(s):
            if v in d and l <= d[v]:
                l = d[v]+1
            else:
                m = max(m, r-l +1)
            d[v]=r
        return m

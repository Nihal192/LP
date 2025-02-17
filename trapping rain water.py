from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
      #build aux arrays

      l_wall = r_wall = 0
      n = len(nums)
      max_l = [0]*n
      max_r = [0]*n
      for i in range(n):
        j = -i -1
        max_l[i] = l_wall 
        max_r[j] = r_Wall 

        l_wall = max (l_Wall,height[i])
        r_wall = max (r_wall, height[j])
      summ = 0
      for i in range(n):
        pot = max (max_l[i], max_r[i])
        summ += (0, pot - height[i])

        



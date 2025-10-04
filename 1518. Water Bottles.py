class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
      return numBottles + (numsBottles-1) // (numsExchange-1)

#number bottles - (numsexchange - 1)
        # numsbottles+extra
        """
        numBottles = 15, numExchange = 4
        limit 4 - F,F,F,F   [15-(4-1)] -> [15-3] => 12 so the Extra bottle is 1 here
        limit 4 - F,F,F,F   [12-(4-1)] -> [12-3] => 9 so the Extra bottle is 1 here
        limit 4 - F,F,F,F   [09-(4-1)] -> [09-3] => 6 so the Extra bottle is 1 here
        limit 4 - F,F,F,F   [06-(4-1)] -> [06-3] => 3 so the Extra bottle is 1 here
        anathi agad nai javai as 4 is our limit
        numsbottles+extra
        so 15 + (1+1+1+1) => 19
        """

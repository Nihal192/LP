def maxProfit(self, prices: List[int]) -> int:
profit=0
for i in range(len(prices)):
  if prices[i]<prices[i+1]:
    profit=prices[i]-prices[i+1]
return profit

def class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
      count = Counter()
      items = items1 + items2
      for x,y in item :
        count[x] += y
      return (sorted(count.items))

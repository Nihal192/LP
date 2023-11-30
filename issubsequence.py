def isSubsequence(self, s: str, t: str) -> bool:
  i=0
  j=0
  while i<len(s) and j<len(t):
    if s[i]=j[t]:
      i+=1
      j+=1
else:
    j+=1
  return True if i==len(s) else return False
    

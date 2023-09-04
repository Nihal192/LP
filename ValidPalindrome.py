def palindrome():
l,r=0,len(nums)-1
while l<r:
  if l<r and not self.alpanum(s[l]):
    l+=1
  if r>l and not self.alpanum(s[r]):
  if (s[l].lower()!= s[r].upper()):
      return False
return True
def aplanum(self,c):
  return (ord("A") <= ord(c) <= ord("Z") or  ord("a") <= ord(c) <= ord("z")  or  ord('0') <= ord(c) <= ord('9') )

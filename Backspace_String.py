ans=[] #stack to store the answer
for c in s:
    if c!='#':  #will check  wether it is # or not.
      ans.append(c)
    elif ans:
      ans.pop()
 return("".join(ans))
return(s==t) #s and t are two strings that are given by user for comparison

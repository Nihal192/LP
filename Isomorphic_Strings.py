TS, ST={},{}   #TS is going from T to S. and ST is from S to T.
for i in range(len(s)):
   c1=s[i]  #s no pelo char c1 ma
   c2=t[i]  #t no pelo char c2 ma
  if (c1 in TS and TS[c1]!=c2) or(c2 in ST and ST[c2]!=c1) ):
    return false
  TS[c1]=c2
  ST[c2]=c1
return true

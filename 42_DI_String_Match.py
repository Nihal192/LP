lo,hi=0,len(s)    #two var to start from 0 and size of string
ans=[]   #stack to store ans
for i in s:   #i will iterate through s 
  if i =='I':          #will check for I and append to ans followed by inc the pointer
    ans.append(s)
    lo+=1
  elif i=='D'
    ans.append(d)     #will check for D and append to ans followed by dec the pointer
    hi+=1
 return(ans+[lo])       #will return the ans appended to lo

mergersort(arr,s,m,e):
if e-s+1<=1:
  return arr
mid=s+e//2
mergesort(arr,s,m)
mergesort(arr,m+1,e)
merge(arr,s,m,e)
return arr

mergersort(arr,s,m,e):
 # Copy the sorted left & right halfs to temp arrays
l=arr[s:m+1]
r=arr[m+1:e+1]
i=0
j=0
k=s

while i<len(l) and j<len(r):
  # Merge the two sorted halfs into the original array
  if l[i]<=r[j]:
    arr[k]=l[i]
    i+=1
  else:
    arr[k]= r[j]
    j+1
  k+=1

if i<len(l):
  a[k]=l[i]
  i+=1
  k+=1
elif j<len(r)
  a[k]=r[j]
  i+=1
  k+=1

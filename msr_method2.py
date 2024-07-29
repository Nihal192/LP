last=m+n-1

while m>0 and n>0:
    if nums1[m-1] > nums2[n-1]:
        nums1[last]=nums1[m-1]
        m-=1
    else:
        nums1[last]=nums2[n-1]
        n-=1
    last-=1
while n>0:
    nums1[last]=nums2[n-1]
    n-=1
    last-=1


    #intialize last variable , and set value as m+n-1
    #so we have 2 while checks:  1) m>0 and n>0  and 2) n>0  
    #nums1[last] is the variable where everything is assigned.
    
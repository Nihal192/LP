l=0
r=0
mp=0

while r<len(price):
    if price[l]<price[r]:
        profit = price[r]-price[l]
        mp=max(mp,profit)
    else:
        l=r
    r+=1
return mp


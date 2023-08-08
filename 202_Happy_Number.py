w=set()
while i != 1:
   while n != 1:
            if n in w : return False
            w.add(n)
            n=sum([int(i)**2 for i in str(n)])
        else:
                return True

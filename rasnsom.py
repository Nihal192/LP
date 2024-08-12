def ransom(c1,c2):
    s1=Counter(c1)
    s2=Counter(c2)

    if s1&s2==s1:
        return True
    else:
        return False
    

ransom("aa","aaba")
def lemonade(bills):
    five=0
    ten=0

    for i in range(len(bills)):
        if bills[i]==5:
            five+=1
        elif bills[i]==10:
            if five>=1:
                five-=1
                ten+=1
            else:
                return False
        else:
            if bills[i]==20 and ten>=1 and five>=1 :
                

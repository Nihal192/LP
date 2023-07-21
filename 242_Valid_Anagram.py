class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):  #    FTF apde jovu padse ke banev ni lenght jo same hoi tohj agad vadhvanu i.e Base case
            return False
    #sorting nu major reason che ke apdu conditioning easy thai jase.
        a=sorted(s) 
        b=sorted(t)
        flag=0 #apde ane niche condition pramane use karisu / you can always use counter if required
        for i in range(len(a)): # we have used brute approach by checking condition for every element
            if(a[i]!=b[i]):
                flag=1
                break
        if(flag==0):
            return True
        else:
            return False

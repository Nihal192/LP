class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=collections.defaultdict(list)  #ahiya will map the no.of occurence 
        for s in strs:     #running through every char
            count=[0]*26    #a...z
            for c in s:
                count[ord(c)-ord("a")] += 1  #this will assign a -o , b-1
            res[tuple(count)].append(s) #append the result
        return res.values()
        

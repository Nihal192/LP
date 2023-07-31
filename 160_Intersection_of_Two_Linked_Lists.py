class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2=headA,headB  #START point assign karo banev list ne
        while l1!=l2:      #ahiya it means tame end par aii gaya
              l1=l1.next if l1 else headB  #will check jo l1 is empty to B this start karo
              l2=l2.next if l2 else headA   #will check jo l2 empty hoi toh A thi start thase
        return(l1)

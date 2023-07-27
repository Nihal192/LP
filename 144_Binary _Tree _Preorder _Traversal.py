class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur=root
        stack=[]
        res=[]
        while cur or stack:
            if cur:
                res.append(cur.val)  #ahiya answer store thato rese
                stack.append(cur.right)  #logic paramane righ value ne stack ma pela nakhisu 
                cur=cur.left          #it is code to update the current pointer , it will start from left
            else:
                cur=stack.pop()     #when null encounter thase tyare stack mathi element pop thase .
        return res

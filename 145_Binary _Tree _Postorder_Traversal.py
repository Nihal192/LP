class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,visit = [root],[False]
        res = []   #ahiya will keep track of visited node

        while stack:
            cur, v = stack.pop(), visit.pop()    #pop operation will be assginged of stack and visited node

            if cur:
                if v:
                    res.append(cur.val) #will append the current value  to result 
                else:
                    
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)  #reverse order ma apde childrens ne append karisu
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)

        return res

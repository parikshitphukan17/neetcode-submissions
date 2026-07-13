# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(cur,minVal,maxVal):
            if not cur:
                return True
            if cur.val<=minVal or cur.val>=maxVal:
                return False
            return check(cur.left,minVal,cur.val) and check(cur.right,cur.val,maxVal)
        return check(root,-1001,1001)
        
        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(cur,maxVal,minVal):
            if not cur:
                return True
            if cur.val>=maxVal or cur.val<=minVal:
                return False
            return check(cur.left,cur.val,minVal) and check(cur.right,maxVal,cur.val)
        return check(root,1001,-1001)

   
        
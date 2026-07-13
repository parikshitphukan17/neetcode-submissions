# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(maxVal,minVal,node):
            if not node:
                return True
            if maxVal<=node.val or node.val<= minVal:
                return False
            return check(node.val,minVal,node.left) and check(maxVal,node.val,node.right)
        return check(1001,-1001,root)

        
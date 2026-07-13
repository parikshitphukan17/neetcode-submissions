# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(n1,n2):
            if not n1 and not n2:
                return True
            if (n1 and not n2) or (n2 and not n1):
                return False
            if n1.val != n2.val:
                return False
            return same(n1.left,n2.left) and same(n1.right,n2.right)
        
        def isSub(n1,n2):
            if not n1:
                return False
            if same(n1,n2):
                return True
            return isSub(n1.left,n2) or isSub(n1.right,n2)
        return not subRoot or isSub(root,subRoot)
            

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def isBalanced(node):
            if not node or not self.balanced:
                return 0
            left = isBalanced(node.left)
            right = isBalanced(node.right)
            if not self.balanced or abs(right -left)>1:
                self.balanced = False
                return 0
            return 1 + max(left,right)
        isBalanced(root)
        return self.balanced
            


            


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        while q:
            lev = []
            child = []
            while q:
                node = q.pop(0)
                if node.left:
                    child.append(node.left)

                if node.right:
                    child.append(node.right)
                lev.append(node.val)
            res.append(lev)
            q = child
        return res
            

                


        
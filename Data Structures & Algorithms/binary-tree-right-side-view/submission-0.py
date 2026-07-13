# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def fillChild(node,child):
            if node.left:
                child.append(node.left)
            if node.right:
                child.append(node.right)

        q = [root]
        res = []
        while q:
            child = []
            last = q.pop()
            res.append(last.val)
            while q:
                fillChild(q.pop(0),child)
            fillChild(last,child)
            q = child
        return res

            


        
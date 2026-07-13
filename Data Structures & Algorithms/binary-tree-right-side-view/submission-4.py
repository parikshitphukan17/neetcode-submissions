# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        q = deque([root])
        while q:
            child = deque([])
            right = None
            while q:
                right = q.popleft()
                if right.left:
                    child.append(right.left)
                if right.right:
                    child.append(right.right)
            res.append(right.val)
            q = child
        return res
                
        
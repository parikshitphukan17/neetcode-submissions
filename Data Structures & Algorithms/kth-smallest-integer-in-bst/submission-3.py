# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        stack = []
        node = root
        while node:
            while node:
                stack.append(node)
                node = node.left
            n = None
            while stack:
                k-=1
                n = stack.pop()
                if k == 0:
                    return n.val
                if n.right:
                    break
            node = n.right
        
            


#         k= 8

#          4
#     3           8
# 2           7.      10
#         6          9   
#         5

#  while node
#    stack.append(node)
#    node =node.left
#  start poping till there is right then make that node and repeat
#  each pop k-=1
#  if k == 0:
#     return popped val
       
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        self.res = None

        def kth(cur):
            nonlocal k
            if not cur or self.res !=None:
                return
            kth(cur.left)
            print(cur.val)
            stack.append(cur.val)
            smallest = None
            while k>0 and stack:
                smallest = stack.pop()
                k -=1
            print(k,stack,smallest)
            if k == 0 and self.res ==None:
                self.res = smallest
                return
            kth(cur.right)
        kth(root)
        return self.res
            


                
            


            





#                             9  
#                 6                       11
#                         8            10
#             5       7
#         4
#     3
# 2            






# [2,3,4,5,6,7,8,9,10,11]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list = []
        self.res = None
        def dfs(node):
            nonlocal k
            if not node:
                return
            dfs(node.left)
            list.append(node)
            small = None
            while list and k>0:
                small = list.pop(0)
                k -=1
            if k ==0 and small:
                self.res =  small.val
                return
            dfs(node.right)
        dfs(root)
        return self.res
                


        #                     4
                
        #         2
        #                                    6
        # 1           3               5

        #reach leftmost node
        #insert into a list and backtrak till there is a right node
        #once found keep poping till list not empty and k>0
        #if k greater than 0 go left most and repeat

        # k = 5
        # [1,2].
        # k = 3
        # [3]
        # k = 2
        # [4]

        # k=1
        # [5,6] 

        



        
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(cur,next):
            if not cur:
                return
            cur.next = next
            dfs(cur.left,cur.right)
            leftNext = None
            if next:
                leftNext = next.left

            dfs(cur.right,leftNext)
        dfs(root,None)
        return root

      




        


        #                         1
        #             2                           3
        #     4               5           6               7

        # 8       9       10      11.  12     13      14      15





        
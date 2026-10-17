"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dp = {}
        def copy(node):
            if not node:
                return
            if node in dp:
                return dp[node]
            cp = Node(node.val,None,None)
            dp[node] = cp
            cp.next = copy(node.next)
            cp.random = copy(node.random)
            return cp
        return copy(head)
            
        
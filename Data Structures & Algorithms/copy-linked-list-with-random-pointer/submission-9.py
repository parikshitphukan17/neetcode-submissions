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
        def dfs(node):
            if not node:
                return node
            if node in dp:
                return dp[node]
            dp[node] = Node(node.val)
            dp[node].next = dfs(node.next)
            dp[node].random = dfs(node.random)
            return dp[node]
        return dfs(head)


        
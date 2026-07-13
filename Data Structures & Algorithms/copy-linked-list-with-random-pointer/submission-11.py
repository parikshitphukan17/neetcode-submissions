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
        def dfs(cur):
            if not cur:
                return
            if cur in dp:
                return dp[cur]
            copy = Node(cur.val)
            dp[cur] = copy
            copy.next = dfs(cur.next)
            copy.random= dfs(cur.random)
            return copy
        return dfs(head)
        
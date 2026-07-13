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
        cache = {}
        def dfs(node):
            if not node:
                return None
            if node in cache:
                return cache[node]
            n = Node(node.val)
            cache[node] = n
            n.next = dfs(node.next)
            n.random = dfs(node.random)
            return n
        return dfs(head)
            
        
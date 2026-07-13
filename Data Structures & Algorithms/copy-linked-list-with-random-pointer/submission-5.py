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
        copy = {}
        def dfs(cur):
            if not cur:
                return None
            if cur in copy:
                return copy[cur]
            copyNode = Node(cur.val)
            copy[cur] = copyNode
            copyNode.next = dfs(cur.next)
            copyNode.random = dfs(cur.random)
            return copyNode
        return dfs(head)
        
        
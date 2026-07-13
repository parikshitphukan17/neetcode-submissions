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
        if not head:
            return None
        cache = {}
        cur1 = head
        while cur1:
            cpy = Node(cur1.val)
            cache[cur1] = cpy
            cur1 = cur1.next
        cur1 = head
        while cur1:
            cpy = cache[cur1]
            if cur1.next:
                cpy.next = cache[cur1.next]
            if cur1.random:
                cpy.random = cache[cur1.random]
            cur1 = cur1.next
            
        return cache[head]


            
            

        
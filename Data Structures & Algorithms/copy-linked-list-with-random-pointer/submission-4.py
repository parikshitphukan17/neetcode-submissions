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
            return 
        cache = {}
        cur = head
        while cur:
            copy = Node(cur.val,cur.next)
            cache[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = cache[cur]
            if cur.next:
                copy.next = cache[cur.next]
            if cur.random:
                copy.random = cache[cur.random]
            cur = cur.next
        return cache[head]


        
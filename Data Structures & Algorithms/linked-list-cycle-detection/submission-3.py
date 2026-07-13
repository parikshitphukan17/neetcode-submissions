# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        cur,fast = head,head.next
        while fast and fast.next:
            if cur == fast:
                return True
            cur,fast = cur.next,fast.next.next
        return False
        
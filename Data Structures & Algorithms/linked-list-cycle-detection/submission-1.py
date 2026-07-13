# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur,fast = head,head.next
        while fast and fast.next:
            if fast == cur:
                return True
            cur = cur.next
            fast = fast.next.next
        return False
        
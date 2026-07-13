# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n= None
        cur = head
        while cur:
            nxt = cur.next
            cur.next= n
            n= cur
            cur = nxt
        return n
        
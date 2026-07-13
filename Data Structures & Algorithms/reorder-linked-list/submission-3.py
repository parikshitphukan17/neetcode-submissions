# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        cur1,cur2 = head,head
        while cur2 and cur2.next:
            cur1 = cur1.next
            cur2 = cur2.next.next
        cur = cur1.next
        cur1.next = None
        n = None
        while cur:
            nxt = cur.next
            cur.next = n
            n = cur
            cur =nxt
        cur1,cur2 = head,n
        dummy = ListNode(-1)
        cur = dummy
        while cur1 and cur2:
            nxt1,nxt2 = cur1.next,cur2.next
            cur1.next = cur2
            cur.next = cur1
            cur = cur2
            cur1,cur2 = nxt1,nxt2
        if cur1:
            cur.next = cur1
            



        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur1 ,cur2 = head,prev
        while cur2:
            nxt1,nxt2 = cur1.next,cur2.next
            cur1.next = cur2
            cur2.next = nxt1
            cur1 = nxt1
            cur2= nxt2

      




        



       








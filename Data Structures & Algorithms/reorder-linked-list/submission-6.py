# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        cur,fast = head,head.next
        if not fast:
            return 
        while fast and fast.next:
            cur = cur.next
            fast = fast.next.next
        cur2 = cur.next
        cur.next = None

        nxt = None
        while cur2:
            nxtCur2 = cur2.next
            cur2.next = nxt
            nxt = cur2
            cur2 = nxtCur2
        cur2 = nxt
        cur1 = head
        while cur1 and cur2:
            nxt1,nxt2 = cur1.next,cur2.next
            cur1.next = cur2
            cur2.next = nxt1
            cur1,cur2 = nxt1,nxt2
        








        #    c. c  c     h.    h.      
        # c  h.    h
        # 0, 1, 2, 3, 4, 5, 6

        # reverse from c.next
        # c.next = None


        # 0, 1, 2, 3 
        # 6, 5, 4
        # 0->6->1->5->2->4->3

        #    c. c
        # c. h.    h.    h
        # 0, 1, 2, 3, 4, 5

        
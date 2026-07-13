# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        if not slow:
            return
        fast = head.next
        if not fast or not fast.next:
            return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        nextHead = slow.next
        slow.next = None
        prev = None
        while nextHead:
            next = nextHead.next
            nextHead.next = prev
            prev = nextHead
            nextHead = next
        cur1,cur2 = head,prev
        while cur2:
            n1,n2 = cur1.next,cur2.next
            cur1.next = cur2
            cur2.next = n1
            cur1,cur2 = n1,n2
        
        





        #     f       f       f
        # s.  s   s          
        # 1   2   3   4   5

        # 1   5   2   4   3

        #     f       f
        # s   s
        # 1   2   3   4

        #     f
        # s
        # 1   2
        #     f       f
        # s   s
        # 1   2   3


        
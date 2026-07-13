# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1,cur2 = l1,l2
        c = 0
        tmpHead = ListNode()
        cur = tmpHead
        while cur1 or cur2 or c:
            s = (cur1.val if cur1 is not None else 0) + (cur2.val if cur2 is not None else 0) +c
            if s<10:
                node = ListNode(s)
                cur.next = node
                c = 0
            else:
                c = s//10
                s = s%10
                node = ListNode(s)
                cur.next = node
            cur = cur.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        return tmpHead.next
     







        
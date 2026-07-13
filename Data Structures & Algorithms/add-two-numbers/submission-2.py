# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        carry,cur1,cur2 = 0,l1,l2
        dummy = ListNode(0)
        cur = dummy
        while cur1 and cur2:
            s = cur1.val + cur2.val + carry
            carry = 0
            if s>=10:
                carry = s//10
                s = s%10
            cur.next = ListNode(s)
            cur = cur.next
            cur1,cur2 = cur1.next, cur2.next

        while cur1:
            s = cur1.val + carry
            carry = 0
            if s>=10:
                carry = s//10
                s = s%10
            cur.next = ListNode(s)
            cur = cur.next
            cur1 = cur1.next

        while cur2:
            s = cur2.val + carry
            carry = 0
            if s>=10:
                carry = s//10
                s = s%10
            cur.next = ListNode(s)
            cur = cur.next
            cur2 = cur2.next
        
        if carry:
            cur.next = ListNode(carry)
        return dummy.next

            
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0)
        prev = tmp
        carry = 0
        while l1 or l2 or carry:
            s1 = 0 if not l1 else l1.val
            s2 = 0 if not l2 else l2.val
            s = s1+s2+carry
            carry = s//10
            s = s%10
            prev.next = ListNode(s)
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return tmp.next
            


    
        
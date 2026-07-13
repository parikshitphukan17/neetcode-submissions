# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1,cur2 = l1,l2
        carry = 0
        dummy = ListNode(-1)
        cur = dummy
        while cur1 or cur2 or carry:
            n1 = cur1.val if cur1 else 0
            n2 = cur2.val if cur2 else 0
            s = n1+n2+carry
            if s>9:
                carry = math.floor(s/10)
                s = s%10
            else:
                carry = 0
            node = ListNode(s)
            cur.next = node
            cur = node
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        return dummy.next
            
            

        
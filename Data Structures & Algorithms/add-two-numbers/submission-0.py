# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1,cur2 = l1,l2
        tempHead = ListNode()
        cur = tempHead
        carry = s = 0
        while cur1 and cur2:
            s = cur1.val+cur2.val + carry
            if s>9:
                carry = s//10
                s = s%10
            else:
                carry = 0
            newNode = ListNode(s)
            cur.next = newNode
            cur = newNode
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            s = cur1.val+carry
            if s>9:
                carry = s//10
                s = s%10
            else:
                carry = 0
            newNode = ListNode(s)
            cur.next = newNode
            cur = newNode
            cur1 = cur1.next
        while cur2:
            s = cur2.val+carry
            if s>9:
                carry = s//10
                s = s%10
            else:
                carry = 0
            newNode = ListNode(s)
            cur.next = newNode
            cur = newNode
            cur2 = cur2.next
        if carry:
            cur.next = ListNode(carry)



        return tempHead.next
            

        
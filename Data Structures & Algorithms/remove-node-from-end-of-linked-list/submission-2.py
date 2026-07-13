# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        cur2 = head
        while n:
            cur2 = cur2.next
            n -= 1
        if not cur2:#remove head
            return head.next
        cur1 = head
        while cur2.next:
            cur1 = cur1.next
            cur2 = cur2.next
        cur1.next= cur1.next.next
        return head

        

        
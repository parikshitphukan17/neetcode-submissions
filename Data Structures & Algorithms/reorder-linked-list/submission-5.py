# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next:
            slow,fast = head,head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            cur = slow.next
            slow.next = None
            last = None
            while cur:
                next = cur.next
                cur.next = last
                last = cur
                cur = next
            
            cur1,cur2 = head,last
            while cur1 and cur2:
                next1,next2 = cur1.next,cur2.next
                cur1.next = cur2
                cur2.next = next1
                cur1,cur2 = next1,next2


        
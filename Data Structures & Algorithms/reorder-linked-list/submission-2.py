# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur,fast = head,head.next
        while fast and fast.next:
            cur = cur.next
            fast = fast.next.next
        curHead = cur.next
        cur.next = None
        cur,last = curHead,None

        while cur:
            nxt = cur.next
            cur.next= last
            last = cur
            cur = nxt
        cur1,cur2 = head,last
        while cur1 and cur2:
            n1,n2 = cur1.next,cur2.next
            cur1.next = cur2
            cur2.next = n1
            cur1,cur2 = n1,n2
        
        



            
        
        
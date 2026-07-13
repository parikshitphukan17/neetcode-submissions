# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        nxt = None
        while cur:
            tmp = cur
            tmpNext = cur.next
            cur.next = nxt
            cur = tmpNext
            nxt = tmp
        return tmp

        
        
        # 1->2->3->4

        # cur = 1, 2
        # nxt = 2, 1
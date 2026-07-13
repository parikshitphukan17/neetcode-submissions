# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        tmpNode = ListNode(0,head)

        r = tmpNode
        while n>0:
            n-=1
            r = r.next
        
        l = tmpNode
        while r.next:
            l=l.next
            r=r.next
        l.next = l.next.next
        return tmpNode.next


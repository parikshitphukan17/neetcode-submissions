# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = ListNode(0,head)
        r = temp
        while n>=0:
            r = r.next
            n-=1
        
        l = temp
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return temp.next





        
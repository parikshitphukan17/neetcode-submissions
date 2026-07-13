# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmpNode = ListNode(0,head)
        cur = tmpNode
        while n>0:
            cur = cur.next
            n-=1
        left = tmpNode
        while cur.next:
            cur = cur.next
            left = left.next
        left.next = left.next.next
        return tmpNode.next
        




        #     c   c
        # h,1,2,3,4  

        #           c
        # h,1,2,3,4,5

        # c.  c
        # h,1,2





        
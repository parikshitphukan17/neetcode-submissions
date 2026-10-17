# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next and head.next.next:
            
            cur,fast = head,head.next
            while fast and fast.next:
                cur,fast = cur.next,fast.next.next
            
            rev = cur.next
            cur.next = None

            prev = None
            cur = rev
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            
            cur = head
            revCur = prev
            while revCur:
                n1, n2 = cur.next,revCur.next
                cur.next = revCur
                revCur.next = n1
                cur,revCur = n1,n2



        #     f       f
        # c   c
        # 0   1   2   3


        # 0   1
        # 3   2
        # 0   3   1   2

        # 0   3   1   2

        #     f       f       f
        # c   c   c
        # 0   1   2   3   4

        # 0   1   2
        # 4   3
        # 0   4   1   3   2

        # 0   4   1   3   2

        # c   f
        # 0   1

        # if not head or head.next or not head.next.next:
        #     return
        #     f       f
        # c   c
        # 0   1   2

        # 0   2   1


        # 0   1   2

        # 4   3
        # 0   4   1   3   2

        
        # 0   1   2
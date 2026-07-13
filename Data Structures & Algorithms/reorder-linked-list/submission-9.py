# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return 
        s,f = head,head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        c2 = s.next
        s.next = None
        next = None
        while c2:
            c2Next = c2.next
            c2.next = next
            next = c2
            c2 = c2Next
        

        c1,c2 = head,next

        while c1 and c2:
            c1Next,c2Next = c1.next,c2.next
            c1.next = c2
            c2.next = c1Next
            c1,c2 = c1Next,c2Next
            



        # rev c.next


        #     c
        # c   f       f
        # 0   1   2   3

        # c1
        # 0   1
        # c2
        # 3   2


        # prev = tempNode


        # prev = prev.next = c1

        # c1 -> c2
        # prev = c2
        # c1 -> c1.next
        # c2 = c2.next

        #     c   c               f
        # c   f       f
        # 0   1   2   3   4



        # 0->1->2

        # 4->3

        # tmpNode
        # tmpNode-> c1
        # c1-> c2
        # c1->c1.next
        # c2->c2.next 
        #     c
        # c.  f       f   
        # 0   1   2


        # 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKth(node,k):
            i = 0
            while node and i<k-1:
                node = node.next
                i+=1
            return node
        
        def reverse(node):
            n = None
            while node:
                next = node.next
                node.next = n
                n = node
                node = next
            return n

        dummy = ListNode(-1)
        prevHead = dummy
        cur = head
        while cur:
            kth = getKth(cur,k)
            if not kth:
                prevHead.next = cur
                break
            nextHead = kth.next
            kth.next = None
            newHead= reverse(cur)
            prevHead.next = newHead
            prevHead = cur
            cur = nextHead
        return dummy.next


                
        
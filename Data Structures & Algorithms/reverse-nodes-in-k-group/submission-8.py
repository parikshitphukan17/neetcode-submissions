# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmpNode = ListNode()
        prev = tmpNode
        cur = head
        def getKth(node,k):
            while k>1 and node:
                node = node.next
                k-=1
            return node
        def reverse(node):
            prev = None
            while node:
                print
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev
        while cur:
            kth = getKth(cur,k)
            if not kth:
                prev.next = cur
                break
            nextHead = kth.next
            kth.next = None
            revHead = reverse(cur)
            prev.next = revHead
            prev = cur
            cur = nextHead

            
        return tmpNode.next

        
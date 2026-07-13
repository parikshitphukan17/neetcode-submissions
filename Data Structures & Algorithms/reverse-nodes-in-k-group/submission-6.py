# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getkthNode(cur,k):
            while k>1 and cur:
                cur = cur.next
                k-=1
            return cur
        def reverse(cur,prevHead):
            prev = None
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            prevHead.next = prev
        temp = ListNode()
        prev = temp
        cur = head
        while cur:
            kthNode = getkthNode(cur,k)
            if not kthNode:
                prev.next = cur
                break
            nextCur = kthNode.next
            kthNode.next = None
            nextPrev= cur
            reverse(cur,prev)
            cur = nextCur
            prev = nextPrev
        return temp.next






        
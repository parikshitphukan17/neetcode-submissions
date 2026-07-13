# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(node):
            next = None
            while node:
                nextCur = node.next
                node.next = next
                next = node
                node = nextCur
            return next  

        def jump(node,k):
            while k>1 and node and node.next:
                node = node.next
                k-=1
            print(k,node)
            if k>1:
                return None
            return node
            

        tmpHead = ListNode()
        cur = head
        prevTail = tmpHead
        while cur:
            kth = jump(cur,k)
            if not kth:
                prevTail.next = cur
                break
            nxtGroup = kth.next
            
            kth.next = None
            revNode = rev(cur)

            prevTail.next = revNode

            prevTail = cur
            cur = nxtGroup
        return tmpHead.next


        
        
        








        # keep track of prevTail to connect to
        # then jump k nodes ahead from cur
        # detach this node from next group also store next group head in temp
        # reverse this group
        # connect prevHead with first of this group
        # makePrevTail now cur since its last
        # make cur = tmp







        
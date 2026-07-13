# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        def check(node):
            cnt = k
            while cnt>1 and node:
                node = node.next
                cnt -=1
            return node
        
        def reverse(node):
            prev = None
            cur = node
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        tmpNode = ListNode(0)
        prev = tmpNode
        cur = head
        while cur:
            kth = check(cur)
            if not kth:
                prev.next = cur
                break
            nextCur = kth.next
            kth.next = None
            nextPrev = cur
            revNode = reverse(cur)
            prev.next = revNode
            prev = nextPrev
            cur = nextCur
        return tmpNode.next




        #prev = tempNodeHead
        #loop
        #check if enough nodes
            #no then just connect to prev and end loop
        #check should also return kth node
        #store kth + 1 node as next batch
        #store currentHead as prev for next batch
        #rev next k nodes
        #connect prev to head of rev node
        #make next prev as current prev
        #move to next batch

        
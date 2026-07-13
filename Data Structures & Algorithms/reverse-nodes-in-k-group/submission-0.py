# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = ListNode(0,head)
        prevHead,cur = temp, head
        def getKth(node,count):
            while node and count>1:
                node = node.next
                count -=1
            if count >1:
                return None
            return node
        
        def reverse(node,kthNode,previousHead):
            print("reversing")
            prev =None
            while node:
                print(node.val)
                if prev:
                    print("prev",prev.val)
                nxt = node.next
                node.next = prev
                prev = node
                print("prev",prev)
                if node == kthNode:
                    break
                node = nxt
                

            previousHead.next = kth

        while True:
            if prevHead:
                print("prevHead",prevHead.val)
            kth = getKth(cur,k)
            if not kth:
                return temp.next
            print("kth",kth.val)
            
            newgroup = kth.next
            if newgroup:
                print("newGroup",newgroup.val)
            reverse(cur,kth,prevHead)
            curCopy =kth
            while  curCopy:
                print("rev",curCopy.val)
                curCopy = curCopy.next
            prevHead.next = kth
            prevHead = cur
            cur.next = newgroup
            cur = newgroup

        

        

        
        
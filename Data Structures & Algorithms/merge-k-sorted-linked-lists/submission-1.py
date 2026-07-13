# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(cur1,cur2):
            dummy = ListNode(-1)
            cur = dummy
            while cur1 or cur2:
                if cur1 and not cur2:
                    cur.next = cur1
                    break
                if cur2 and not cur1:
                    cur.next = cur2
                    break
                if cur1.val<cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            return dummy.next
        linkedList = lists
        while len(linkedList)>1:
            newLinkedList = []
            for i in range(0,len(linkedList),2):
                n1 = linkedList[i]
                n2 = linkedList[i+1] if i+1<len(linkedList) else None
                newLinkedList.append(merge(n1,n2))
            linkedList = newLinkedList
        return linkedList[0] if linkedList else  None
                
        
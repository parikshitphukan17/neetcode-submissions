# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        def merge(l1,l2):
            if not l2:
                return l1
            temp = ListNode()
            prev = temp
            cur1,cur2 = l1,l2
            while cur1 and cur2:
                if cur1.val<cur2.val:
                    prev.next = cur1
                    cur1 = cur1.next
                else:
                    prev.next = cur2
                    cur2 = cur2.next
                prev = prev.next
            if cur1:
                prev.next = cur1
            elif cur2:
                prev.next = cur2
            return temp.next
        
        while len(lists)>1:
            nextList = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = None if i+1==len(lists) else lists[i+1]
                mergedList = merge(l1,l2)
                if mergedList:
                    nextList.append(mergedList)
            lists = nextList
        return lists[0] if lists else None


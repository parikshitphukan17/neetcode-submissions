# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return
        def mergeList(l1,l2):
            if not l2:
                return l1
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                n1,n2 = l1.next,l2.next
                if l1.val<l2.val:
                    cur.next = l1
                    l1 = n1
                else:
                    cur.next =l2
                    l2 = n2
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next
        
        lists
        while len(lists)>1:
            mergedList = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 <len(lists) else None
                merged = mergeList(list1,list2)
                mergedList.append(merged)
            lists = mergedList
        return lists[0]
        
                    

                    
             
        
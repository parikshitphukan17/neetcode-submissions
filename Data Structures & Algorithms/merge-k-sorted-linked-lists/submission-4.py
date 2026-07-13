# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1,l2):
            temp = ListNode(0)
            cur = temp
            while l1 and l2:
                if l1.val<l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return temp.next
        
        while len(lists)>1:
            nextLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = None if i+1>= len(lists) else lists[i+1]
                nextLists.append(merge(l1,l2))
            lists = nextLists
        return lists[0] if lists else None

            




        
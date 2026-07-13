# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummy = ListNode(-1)
        cur = dummy
        if not cur1 and not cur2:
            return None
        while cur1 or cur2:
            if (not cur1 and cur2) or (cur1 and cur2 and cur2.val<cur1.val):
                cur.next = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur1 = cur1.next
                
            cur = cur.next
        return dummy.next
        


        
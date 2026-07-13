/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode tempHead = new ListNode();
        var cur = tempHead;
        while(list1!=null || list2!=null){
            if(list1!=null && list2!=null){
                ListNode minNode = null;
                if(list1.val<list2.val){
                    minNode = list1;
                    list1 = list1.next;
                } else {
                    minNode = list2;
                    list2 = list2.next;
                }
                cur.next = minNode;
                cur = cur.next;
            } else if(list1!=null){
                    
                cur.next = list1;
                break;
            } else {
                cur.next = list2;
                break;
            }
        }
        return tempHead.next;
        
    }
}
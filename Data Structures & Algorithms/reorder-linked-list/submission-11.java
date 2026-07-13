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
    public void reorderList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null){
            return ;
        }
        // ListNode temp = new ListNode();
        // temp.next = head;
        // ListNode slow = temp,fast = temp;
        ListNode slow = head,fast = head;
        while(fast!=null && fast.next!=null) {
            slow = slow.next;
            fast = fast.next.next;

        }
        var reverseCur = slow.next;
        slow.next = null;
        ListNode prev= null;
        while(reverseCur!=null){
            var next = reverseCur.next;
            reverseCur.next = prev;
            prev = reverseCur;
            reverseCur = next;
        }
        var cur1 = head;
        var cur2 = prev;
        while(cur1!=null && cur2!=null) {
            var next1 = cur1.next;
            var next2= cur2.next;
            cur1.next = cur2;
            cur2.next = next1;
            cur1 = next1;
            cur2 = next2;
        }
        
        // f           f       f       f
        // s       s   s   s
        // temp    0   1   3   4   5

        // 0   5   1   4   3

        // f           f       f
        // s       s   s       
        // temp    0   1   3   4
        // s       s
        // f           f       f
        // s       s   s
        // temp    0   1   2

        // 0->2->1




        
    }
}

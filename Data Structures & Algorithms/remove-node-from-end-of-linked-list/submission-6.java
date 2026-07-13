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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = new ListNode();
        temp.next = head;
        var right = temp;
        while(n-- >0){
            right = right.next;
        }
        var left = temp;
        while(right.next!=null){
            left = left.next;
            right = right.next;
        }
        left.next = left.next.next;
        return temp.next;




        // s               f
        // 4   3   2   1   0
        // t   1   2   3   4
        //     f
        // 1   0
        // t   5


        // s   s           l
        // 3   2   1   0
        // t   1   2   3   4

        // 1   3   4

        //         l   l   l
        // s   s   s
        // 2   1   0
        // t   1   2   3   4

        // 1 2 4



    }
}

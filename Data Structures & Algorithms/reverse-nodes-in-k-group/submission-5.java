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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode tail = new ListNode();
        var temp = tail;
        var cur = head;
        while(true){
            var kthNode = check(cur,k);
            if(kthNode == null){
                tail.next = cur;
                break;
            }
            var nextCur = kthNode.next;
            var tempTail = cur;
            kthNode.next =null;
            var reverseHead = reverse(cur);
            tail.next = reverseHead;
            cur = nextCur;
            tail = tempTail;
        }
        return temp.next;



        //check k nodes exists from cur
        //if no just connect tail with cur and return
        //save kth +1 as tempNextCur
        //save cur as tempNextTail
        //disconnect kth+1 from kth
        //reverse nodes till kth
        //connect tail to reversed 1st node
        //make tempNextTail as tail
        //make  tempNextCur cur
        //repeat
        
    }

    public ListNode reverse(ListNode cur){
        ListNode prev = null;
        while(cur!=null){
            var next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    public ListNode check(ListNode cur,int k){
        while(k-->1 && cur!=null){
            cur = cur.next;
        }
        return cur;
    }
}

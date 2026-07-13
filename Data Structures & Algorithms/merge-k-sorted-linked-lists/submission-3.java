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
    public ListNode mergeKLists(ListNode[] lists) {
        while(lists.length>1){
            List<ListNode> list = new ArrayList<>();
            for(int i=0;i<lists.length;i+=2){
                ListNode l1 = lists[i];
                ListNode l2 = i+1<lists.length?lists[i+1]:null;
                list.add(merge(l1,l2));
            }
            lists = list.stream().toArray(ListNode[]::new);

        }
        return lists.length>0?lists[0]:null;


    }

    public ListNode merge(ListNode l1,ListNode l2){
        if(l2==null){
            return l1;
        }
        ListNode tempHead = new ListNode();
        var prev = tempHead;
        while(l1!=null || l2!=null){
            if(l1 !=null && l2 != null){
                if(l1.val<l2.val){
                    prev.next = l1;
                    l1 = l1.next;
                } else {
                    prev.next = l2;
                    l2 = l2.next;
                }
                prev = prev.next;

            } else if(l1!=null){
                prev.next = l1;
                break;
            } else {
                prev.next = l2;
                break;
            }
        }
        return tempHead.next;
        
    }


}

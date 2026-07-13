/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    Map<Node,Node> map = new HashMap<>();

    public Node copyRandomList(Node head) {
        return deepCopy(head);

        
        
    }

    public Node deepCopy(Node node){
        if(node == null){
            return null;
        }
        if(map.containsKey(node)){
            return map.get(node);
        }
        var copy = new Node(node.val);
        map.put(node,copy);
        copy.next = deepCopy(node.next);
        copy.random = deepCopy(node.random);
        return copy;
    }
}

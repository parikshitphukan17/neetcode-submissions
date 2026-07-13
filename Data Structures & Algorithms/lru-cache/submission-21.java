class Node{
    Node next = null;
    Node prev = null;
    int value = 0;
    int key = 0;
    public Node(int key,int value){
        this.key = key;
        this.value = value;
    }
}



class LRUCache {
    
    int cap,cur;
    Node head,tail;
    Map<Integer,Node> map = new HashMap<>();
    public LRUCache(int capacity) {
        cap = capacity;
        cur = 0;
        head = new Node(0,0);
        tail = new Node(0,0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            var node = remove(key);
            add(key,node.value);
            return map.get(key).value;
        }
        return -1;
    }

    public Node remove(int key) {
        var node = map.remove(key);
        var prev = node.prev;
        var next = node.next;
        prev.next = next;
        next.prev = prev;
        cur--;
        return node; 
    }

    public Node add(int key, int value){
        if(map.containsKey(key)){
            remove(key);
        }
        var node = new Node(key,value);
        map.put(key,node);
        var prev = head;
        var next = head.next;
        prev.next = node;
        next.prev = node;
        node.next = next;
        node.prev = prev;
        cur++;
        return node;
    }
    
    public void put(int key, int value) {
        add(key,value);
        if(cap<cur){
            remove(tail.prev.key);
        }
    }
}

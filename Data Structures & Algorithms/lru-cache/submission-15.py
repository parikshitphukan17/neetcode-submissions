class Node:
    def __init__(self,val = 0,key=0, nxt= None, prev = None):
        self.nxt = nxt
        self.val = val
        self.prev = prev
        self.key =key


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.nxt,self.tail.prev = self.tail,self.head
        self.cur = 0
        self.pointer = {}
        

    def get(self, key: int) -> int:
        if key not in self.pointer:
            return -1
        node = self.pointer[key]
        if self.head.nxt == node:
            return node.val
        prev,nxt = node.prev,node.nxt 
        prev.nxt,nxt.prev = nxt,prev
        nxtHead = self.head.nxt
        self.head.nxt,node.prev = node,self.head
        node.nxt,nxtHead.prev = nxtHead,node
        

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.pointer:
            node = self.pointer[key]
            prev,nxt = node.prev,node.nxt 
            prev.nxt,nxt.prev = nxt,prev
            del self.pointer[key]
            self.cur -=1
        nxtHead = self.head.nxt
        node = Node(value,key,nxtHead,self.head)
        self.head.nxt,nxtHead.prev = node,node
        self.pointer[key] = node
        self.cur +=1
        while self.cur > self.cap:
            last = self.tail.prev
            prev = last.prev
            del self.pointer[last.key]
            prev.nxt,self.tail.prev = self.tail,prev
            self.cur -=1
    

        

class Node:

    def __init__(self,key=0,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key




class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node()
        self.tail = Node(0,None,self.head)
        self.head.next = self.tail
        self.map = {}
        self.cur = 0


    def remove(self,key):
        node = self.map.pop(key)
        prev = node.prev
        next = node.next
        prev.next,next.prev = next,prev
        self.cur -=1
        return node


    def add(self,key,val):
        node = Node(key,val)
        next = self.head.next
        prev = self.head
        prev.next,next.prev = node,node
        node.next,node.prev = next,prev
        self.map[key] = node
        self.cur +=1



        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.remove(key)
        self.add(key,node.val)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)
        self.add(key,value)
        if self.cur>self.cap:
            self.remove(self.tail.prev.key)
       
        

class Node:
    def __init__(self,val,key,next= None,prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next,self.tail.prev = self.tail,self.head
        self.map = {}
        self.cap = capacity
        self.size =0

    def delete(self,key):
        if key not in self.map:
            return
        node = self.map[key]
        prev = node.prev
        next = node.next
        prev.next,next.prev = next,prev
        self.map.pop(key)
        self.size -=1
    
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.put(key,self.map[key].val)
        return self.map[key].val
        
        #if present delete
            # add to head and return
        #return -1 if not present
        

    def put(self, key: int, value: int) -> None:
        self.delete(key)
        node = Node(value,key)
        self.map[key] = node
        prev = self.head
        next = self.head.next
        prev.next,next.prev = node,node
        node.prev,node.next = self.head,next
        self.size +=1
        if self.size>self.cap:
            self.delete(self.tail.prev.key)
        #if present delete
            #add to head
        # if size >cap:
        #delete tail prev
        

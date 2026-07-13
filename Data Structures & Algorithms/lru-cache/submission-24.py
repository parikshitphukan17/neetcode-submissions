class Node:
    def __init__(self,value,next,prev,key):
        self.value = value
        self.next = next
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cur = 0
        self.first = Node(0,None,None,0)
        self.last = Node(0,None,None,0)
        self.first.next,self.last.prev = self.last,self.first
        self.map = {}
        

    def delete(self,key):
        node = self.map.pop(key)
        prev,next = node.prev,node.next
        prev.next,next.prev=next,prev
        self.cur -=1
        return node

    def insert(self,key,value):
        node = Node(value,None,None,key)
        self.map[key] = node
        next,prev = self.first.next,self.first
        node.next,node.prev = next,prev
        next.prev, prev.next = node,node
        self.cur +=1
        if self.cur> self.cap:
            self.delete(self.last.prev.key)
    
    
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.delete(key)
        self.insert(node.key,node.value)
        return node.value

        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(key)
        self.insert(key,value)





        # f <-> v1 <-> v2 <-> l

        # get v2 
        #     remove v2
        #     insert v2
        # f <-> v2 <-> v1 <-> l
        # when insert check limit if exceeded remove fro last 



        

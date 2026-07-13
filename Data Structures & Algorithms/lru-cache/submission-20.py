class Node:
    def __init__(self,val = 0,key = 0,next=None,prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev




class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail,self.head
        self.cap = capacity
        self.cur = 0
        self.map = {}
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.delete(node)
        self.add(node)
        return node.val


        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(self.map[key])
        node = Node(value,key)
        self.add(node)
        if self.cur>self.cap:
            self.delete(self.tail.prev)


    def delete(self,node):
        prev,next = node.prev,node.next
        prev.next,next.prev = next,prev
        self.map.pop(node.key)
        self.cur -=1

    
    def add(self,node):
        prev,next = self.head,self.head.next
        prev.next,next.prev = node,node
        node.next,node.prev = next,prev
        self.map[node.key] = node
        self.cur +=1

        


        



  




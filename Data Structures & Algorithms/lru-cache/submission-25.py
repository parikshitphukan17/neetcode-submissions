class Node:
    def __init__(self, key = 0,val = 0, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev




class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head,self.end = Node(),Node()
        self.head.next,self.end.prev = self.end,self.head
        self.cur = 0
        self.capacity = capacity


        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.remove(key)
        self.insert(key,node.val)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.insert(key,value)


    def remove(self,key):
        if key not in self.map:
            return
        node = self.map.pop(key)
        prev,next = node.prev,node.next
        prev.next, next.prev = next,prev
        self.cur -=1
        return node
    
    def insert(self,key,value):
        prev = self.head
        next = self.head.next
        node = Node(key,value,next,prev)
        prev.next,next.prev = node,node
        self.map[key] = node
        self.cur +=1
        if self.cur>self.capacity:
            self.remove(self.end.prev.key)
        return node
    

        


        # limit = 2
        # cur = 0
        # h<->e
        # map = {}

        # put: 
        # remove 
        # then insert new to head to maintain order

        # h<->1<->l
        # cur =1

        # get :
        # if not exists:
        #     return -1
        # remove then insert and return
        

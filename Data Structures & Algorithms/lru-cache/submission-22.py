class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.front = Node(-1,-1)
        self.back = Node(-1,-1)
        self.front.right,self.back.left = self.back,self.front
        self.map = {}
        self.cur = 0

        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.remove(key) 
        self.insert(node.key,node.val)
        return node.val
    
    def remove(self,key):
        node = self.map.pop(key)
        left,right = node.left,node.right
        left.right,right.left = right,left
        self.cur -=1
        return node



    def insert(self,key,val):
        node = Node(key,val)
        nei = self.front.right
        self.front.right,nei.left = node,node
        node.left,node.right = self.front,nei
        self.map[key] = node
        self.cur+=1
        return node


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)
        self.insert(key,value) 
        if self.cur > self.cap:
            self.remove(self.back.left.key)



        

class Node:
    def __init__(self):
        self.child = {}
        self.end = False
    




class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node()
            cur = cur.child[w]
        cur.end = True

    def findNode(self,word):
        cur = self.root
        for w in word:
            if w not in cur.child:
                return
            cur = cur.child[w]
        return cur

    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node and node.end
        

    def startsWith(self, prefix: str) -> bool:
        return self.findNode(prefix) is not None





        # d
        # /   
        # o
        # /
        # g   
        
        
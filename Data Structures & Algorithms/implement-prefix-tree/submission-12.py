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


    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node is not None and node.end
        

    def startsWith(self, prefix: str) -> bool:
        return self.findNode(prefix) is not None

    def findNode(self,prefix):
        cur = self.root
        for w in prefix:
            if w not in cur.child:
                return 
            cur = cur.child[w]
        return cur
        
        
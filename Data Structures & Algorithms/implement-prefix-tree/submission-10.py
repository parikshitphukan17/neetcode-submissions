class Node:
    def __init__(self):
        self.child = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.end = True

    def findNode(self,word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                return
            cur = cur.child[c]
        return cur



    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node is not None and node.end
        

    def startsWith(self, prefix: str) -> bool:
        return self.findNode(prefix) is not None
        
        
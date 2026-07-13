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


    def search(self, word: str) -> bool:
        cur = self.nodeExists(word)
        return cur and cur.end

    def nodeExists(self,word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                return None
            cur = cur.child[c]
        return cur
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.nodeExists(prefix)
        return cur !=None



             
class Node:
    def __init__(self):
        self.child = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = Node()
            node = node.child[w]
        node.end = True
        

    def findNode(self,word):
        node = self.root
        for w in word:
            if w not in node.child:
                return None
            node = node.child[w]
        return node

    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node and node.end


        

    def startsWith(self, prefix: str) -> bool:
        node = self.findNode(prefix)
        return True if node else False
        
        
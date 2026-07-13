class TrieNode:

    def __init__(self):
        self.child = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = TrieNode()
            node = node.child[w]
        node.end = True

    def getPrefixNode(self, word: str):
        node = self.root
        for w in word:
            if w not in node.child:
                return None
            node = node.child[w]
        return node

    def search(self, word: str) -> bool:
        node = self.getPrefixNode(word)
        return True if node and node.end else False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.getPrefixNode(prefix)
        return True if node else False
        
        
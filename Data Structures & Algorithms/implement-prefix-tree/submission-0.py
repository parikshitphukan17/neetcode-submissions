class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TreeNode()
            cur = cur.children[w]
        cur.word = True

    def returnNode(self,word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                return None
            cur = cur.children[w]
        return cur

    def search(self, word: str) -> bool:
        cur = self.returnNode(word)
        return cur!=None and cur.word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.returnNode(prefix)
        return cur!=None

        
        
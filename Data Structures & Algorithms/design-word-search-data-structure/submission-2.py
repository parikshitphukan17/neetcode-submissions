class Node:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
        

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = Node()
            node = node.child[w]
        node.end = True
    
    def find(self,i,word,node):
        if i == len(word):
            return node.end
        w = word[i]
        if w != ".":
            if w not in node.child:
                return False
            return self.find(i+1,word,node.child[w])
        for child in node.child:
            if self.find(i+1,word,node.child[child]):
                return True
        return False
        

    def search(self, word: str) -> bool:
        return self.find(0,word,self.root)
        

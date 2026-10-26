class Node:
    def __init__(self):
        self.end = False
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node()
    
    def addWord(self,word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.end = True
    
    def findWord(self,word):

        def search(i,word,node):
            if i == len(word):
                return node.end
            
            if word[i] == ".":
                for child in node.child.values():
                    if search(i+1,word,child):
                        return True
                return False
            if word[i] not in node.child:
                return False
            return search(i+1,word,node.child[word[i]])
        return search(0,word,self.root)
    
            

    

    



class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        self.trie.addWord(word)
        

    def search(self, word: str) -> bool:
        return self.trie.findWord(word)
        

class Node:
    def __init__(self):
        self.end = False
        self.child = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node()
            cur = cur.child[w]
        cur.end = True
        
    def dfs(self,i,word,cur):
        if i == len(word):
            return cur.end
        char = word[i]
        if char == "." or char in cur.child:
            if char == ".":
                for child in cur.child.values():
                    if self.dfs(i+1,word,child):
                        return True
            else:
                return self.dfs(i+1,word,cur.child[char])
        return False

    def search(self, word: str) -> bool:
        return self.dfs(0,word,self.root)


        

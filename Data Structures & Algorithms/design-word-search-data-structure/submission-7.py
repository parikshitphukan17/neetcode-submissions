class Trei:
    def __init__(self):
        self.child = {}
        self.end = False
    
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = Trei()
            cur = cur.child[c]
        cur.end = True
    
    def findWord(self,word):
        N = len(word)
        def dfs(cur,i,word):
            if i==N:
                return cur.end
            if word[i] not in cur.child and word[i] != ".":
                return False
            
            if word[i] != ".":
                return dfs(cur.child[word[i]],i+1,word)
            for child in cur.child.values():
                if dfs(child,i+1,word):
                    return True
            return False
        return dfs(self,0,word)
                    


class WordDictionary:

    def __init__(self):
        self.trei = Trei()
        

    def addWord(self, word: str) -> None:
        self.trei.addWord(word)


        

    def search(self, word: str) -> bool:
        return self.trei.findWord(word)
        

class Trei:
    def __init__(self):
        self.child = {}
        self.end =False

    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = Trei()
            cur = cur.child[c]
        cur.end = True
    

    def search(self,word):
        def dfs(cur,i):
            if i == len(word):
                return cur.end
            if word[i] in cur.child:
                return dfs(cur.child[word[i]],i+1)
            elif word[i] == ".":
                for child in cur.child.values():
                    if dfs(child,i+1):
                        return True
            return False
        return dfs(self,0)




class WordDictionary:

    def __init__(self):
        self.trei = Trei()
        

    def addWord(self, word: str) -> None:
        self.trei.addWord(word)
        

    def search(self, word: str) -> bool:
        return self.trei.search(word)




              
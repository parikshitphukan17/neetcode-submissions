class TreiNode:
    def __init__(self):
        self.child = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TreiNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = TreiNode()
            node = node.child[w]
        node.end = True

    def search(self, word: str) -> bool:
   

        def dfs(i,node):
            if i == len(word):
                return node.end
            if word[i] == ".":
                for parent in node.child:
                    if dfs(i+1,node.child[parent]):
                        return True
            elif word[i] in node.child:
                return dfs(i+1,node.child[word[i]])
            return False
        return dfs(0,self.root)
    



        

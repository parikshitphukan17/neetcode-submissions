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
        
    def dfs(self,node,i,N,word):
        if i == N:
            return node.end
        if word[i] == ".":
            for nei in node.child.values():
                if self.dfs(nei,i+1,N,word):
                    return True
        elif word[i] in node.child:
            return self.dfs(node.child[word[i]],i+1,N,word)
        return False

        
        
        

    def search(self, word: str) -> bool:
        return self.dfs(self.root,0,len(word),word)

        
        

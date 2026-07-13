class TreeNode:
    def __init__(self):
        self.child = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = TreeNode()
            cur = cur.child[w]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i == len(word):
                return node.word
            if word[i] == ".":
                for child in node.child.values():
                    if dfs(i+1,child):
                        return True
                return False
            elif word[i] in node.child:
                return dfs(i+1,node.child[word[i]])
            return False
        return dfs(0,self.root)
            
        

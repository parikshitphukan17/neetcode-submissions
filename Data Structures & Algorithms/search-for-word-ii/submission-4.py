class Trie:
    def __init__(self):
        self.child = {}
        self.end = False
    
    def add(self,word):
        node = self
        for w in word:
            if w not in node.child:
                node.child[w] = Trie()
            node = node.child[w]
        node.end = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add(w)
        res = set()
        vis = set()
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        N,M = len(board),len(board[0])
        def dfs(i,j,node,word):
            if (i,j) in vis or i<0 or j<0 or i==N or j ==M or board[i][j] not in node.child:
                return
            vis.add((i,j))
            node = node.child[board[i][j]]
            word += board[i][j]
            if node.end:
                res.add(str(word))
            for dx,dy in dir:
                dfs(i+dx,j+dy,node,word)
            vis.remove((i,j))
        
        for i in range(N):
            for j in range(M):
                dfs(i,j,trie,"")
        return [w for w in res]
            

        
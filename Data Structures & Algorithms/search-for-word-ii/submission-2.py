class Trei:

    def __init__(self):
        self.child = {}
        self.end = False
    
    def add(self,word):
        node = self
        for w in word:
            if w not in node.child:
                node.child[w] = Trei()
            node = node.child[w]
        node.end = True

class Solution:
    def findWords(self, c: List[List[str]], words: List[str]) -> List[str]:
        trei = Trei()
        board = c
        for w in words:
            trei.add(w)
        N,M = len(board),len(board[0])
        vis = set()
        res = set()
        def dfs(i,j,node,word):
            if i < 0 or j<0 or i==N or j==M or (i,j) in vis or board[i][j] not in node.child:
                return
            vis.add((i,j))
            word += board[i][j]
            node = node.child[board[i][j]]
            if node.end:
                res.add(str(word))
            dfs(i+1,j,node,word)
            dfs(i-1,j,node,word)
            dfs(i,j+1,node,word)
            dfs(i,j-1,node,word)
            vis.remove((i,j))
        
        for i in range(N):
            for j in range(M):
                dfs(i,j,trei,"")
        return list(res)



     
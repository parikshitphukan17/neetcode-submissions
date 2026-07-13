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

            


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trei = Trei()
        for w in words:
            trei.addWord(w)
        N,M = len(board),len(board[0])
        vis = set()
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        res = set()
        def dfs(i,j,cur,word):
            if i<0 or i == N or j<0 or j == M or (i,j) in vis or board[i][j] not in cur.child:
                return
            cur = cur.child[board[i][j]]
            vis.add((i,j))
            word += board[i][j]
            if cur.end:
                res.add(word)
            
            for dx,dy in dir:
                dfs(i+dx,j+dy,cur,word)
            vis.remove((i,j))
        for i in range(N):
            for j in range(M):
                dfs(i,j,trei,"")
        return list(res)

            
    
    
        
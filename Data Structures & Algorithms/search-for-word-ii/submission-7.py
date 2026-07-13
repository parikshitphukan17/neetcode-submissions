class Trei:
    def __init__(self):
        self.end = False
        self.child = {}

    def addWord(self,word):
        cur = self
        for w in word:
            if w not in cur.child:
                cur.child[w] = Trei()
            cur = cur.child[w]
        cur.end = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trei()
        for w in words:
            root.addWord(w)
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        res = set()
        N,M = len(board),len(board[0])
        vis = set()
        def dfs(i,j,s,cur):
            if cur.end:
                res.add(s)
            if i==N or j==M or (i,j) in vis or i<0 or j<0 or board[i][j] not in cur.child:
                return
            vis.add((i,j))
            s += board[i][j]
            cur = cur.child[board[i][j]]
            for dx,dy in dir:
                dfs(i+dx,j+dy,s,cur)
            vis.remove((i,j))
        for i in range(N):
            for j in range(M):
                dfs(i,j,"",root)
        return list(res)
                

    
        
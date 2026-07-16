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
        resSet = set()
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        M,N = len(board),len(board[0])
        vis = set()
        def dfs(i,j,cur,word):
            if i<0 or i==M or j<0 or j == N or board[i][j] not in cur.child or (i,j) in vis:
                return
            vis.add((i,j))
            word += board[i][j]
            cur = cur.child[board[i][j]]
            if cur.end:
                resSet.add(word)
            for dx,dy in dir:
                dfs(i+dx,j+dy,cur,word)
            vis.remove((i,j))
        
        for i in range(M):
            for j in range(N):
                dfs(i,j,trei,"")
        return list(resSet)

        
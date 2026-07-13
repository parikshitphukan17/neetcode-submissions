class Trei:

    def __init__(self):
        self.child = {}
        self.end = False
    
    def addWord(self,word):
        node = self
        for w in word:
            if w not in node.child:
                node.child[w] = Trei()
            node = node.child[w]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        trei = Trei()
        res = set()
        for w in words:
            trei.addWord(w)
        N,M = len(board),len(board[0])
        vis = set()
        def dfs(i,j,node,cur):
            if i==N or j == M or i<0 or j<0 or (i,j) in vis or board[i][j] not in node.child:
                return
            vis.add((i,j))
            cur += board[i][j]
            node = node.child[board[i][j]]
            if node.end:
                res.add(str(cur))
            for dx,dy in dire:
                dfs(i+dx,j+dy,node,cur)
            vis.remove((i,j))
        for i in range(N):
            for j in range(M):
                dfs(i,j,trei,"")
        return [w for w in res]
            

        

        
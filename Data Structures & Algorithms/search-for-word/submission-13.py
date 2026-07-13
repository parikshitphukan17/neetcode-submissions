class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        N,M,L = len(board),len(board[0]), len(word)
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(i,j,k):
            if k == L:
                return True
            if i==N or j==M or i<0 or j<0 or (i,j) in vis or board[i][j] != word[k]:
                return False
            vis.add((i,j))
            for dx,dy in dir:
                if dfs(i+dx,j+dy,k+1):
                    return True
            vis.remove((i,j))
            return False
        for i in range(N):
            for j in range(M):
                if dfs(i,j,0):
                    return True
        return False
        

        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        N,M,L = len(board),len(board[0]),len(word)
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,wi):
            if i == N or j == M or i<0 or j<0 or (i,j) in vis or board[i][j] != word[wi]:
                return False
            vis.add((i,j))
            wi+=1
            if wi == L:
                return True
            for dx,dy in dire:
                if dfs(i+dx,j+dy,wi):
                    return True
            vis.remove((i,j))
            return False
        for i in range(N):
            for j in range(M):
                if dfs(i,j,0):
                    return True
        return False
            
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        L,N,M = len(word),len(board),len(board[0])
        def dfs(i,j,w):
            if (i,j) in vis or i < 0 or j < 0 or i ==N or j==M or board[i][j] != word[w]:
                return False
            vis.add((i,j))
            w+=1
            if w == L:
                return True
            for dx,dy in dire:
                if dfs(i+dx,j+dy,w):
                    return True
            vis.remove((i,j))
            return False
        for i in range(N):
            for j in range(M):
                if dfs(i,j,0):
                    return True
        return False

            


        
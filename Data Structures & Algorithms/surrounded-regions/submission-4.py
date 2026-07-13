class Solution:
    def solve(self, board: List[List[str]]) -> None:
        N,M = len(board),len(board[0])
        grid = board
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(i,j):
            if i<0 or j<0 or i ==N or j==M or grid[i][j] != "O":
                return
            grid[i][j] = "T"
            for dx,dy in dir:
                dfs(i+dx,j+dy)
        for i in range(N):
            dfs(i,0)
            dfs(i,M-1)
        for j in range(M):
            dfs(0,j)
            dfs(N-1,j)
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "T":
                    grid[i][j] = "O"
                elif grid[i][j] == "O":
                    grid[i][j] = "X"
        

        
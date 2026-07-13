class Solution:
    def solve(self, board: List[List[str]]) -> None:
        N,M = len(board),len(board[0])
        dire = [[0,1],[1,0],[0,-1],[-1,0]]


        def dfs(i,j):
            if i<0 or i == N or j<0 or j==M or board[i][j] != "O":
                return
            board[i][j] = "T"
            for dx,dy in dire:
                dfs(i+dx,j+dy)
        for i in range(N):
            dfs(i,0)
            dfs(i,M-1)
        for j in range(M):
            dfs(0,j)
            dfs(N-1,j)
        for i in range(N):
            for j in range(M):
                if board[i][j] =="O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
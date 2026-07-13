class Solution:
    def solve(self, board: List[List[str]]) -> None:
        N,M = len(board),len(board[0])
        def dfs(i,j):
            if i<0 or i==N or j<0 or j==M or board[i][j]!="O":
                return
            board[i][j] = "D"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for j in range(M):
            dfs(0,j)
            dfs(N-1,j)
        for i in range(N):
            dfs(i,0)
            dfs(i,M-1)
        
        for i in range(N):
            for j in range(M):
                if board[i][j] =="D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


        
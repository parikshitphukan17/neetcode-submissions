class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M,N = len(board),len(board[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(i,j):
            if i<0 or i==M or j<0 or j==N or board[i][j]!="O":
                return
            board[i][j] = "T"
            for dx,dy in dir:
                dfs(i+dx,j+dy)

        for i in range(M):
            dfs(i,0)
            dfs(i,N-1)
        
        for j in range(N):
            dfs(0,j)
            dfs(M-1,j)
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
            


            

        
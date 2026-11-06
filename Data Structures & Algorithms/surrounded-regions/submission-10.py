class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        M,N = len(board),len(board[0])
        for i in range(M):
            if board[i][0] == "O":
                q.append([i,0])
            if board[i][N-1] == "O":
                q.append([i,N-1])
        for j in range(N):
            if board[0][j] == "O":
                q.append([0,j])
            if board[M-1][j] == "O":
                q.append([M-1,j])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            i,j = q.popleft()
            if i<0 or j<0 or i==M or j==N or board[i][j] != "O":
                continue
            board[i][j] = "T"
            for dx,dy in dir:
                q.append([i+dx,j+dy])
        for i in range(M):
            for j in range(N):
                if board[i][j] =="O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        






        
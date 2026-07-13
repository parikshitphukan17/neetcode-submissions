class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = []
        N,M = len(board), len(board[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(N):
            if board[i][0] == "O":
                q.append([i,0])
            if board[i][M-1] == "O":
                q.append([i,M-1])
        for j in range(1,M-1):
            if board[0][j] == "O":
                q.append([0,j])
            if board[N-1][j] == "O":
                q.append([N-1,j])
        while q:
            nextQ = []
            while q:
                i,j = q.pop()
                if i<0 or j<0 or i==N or j==M or board[i][j] != "O":
                    continue
                board[i][j] = "T"
                for dx,dy in dir:
                    nextQ.append([i+dx,j+dy])
            q = nextQ
        for i in range(N):
            for j in range(M):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"


        

# ["O","X","X","O","X"] ["O","X","X","O","X"]
# ["X","O","O","X","O"] ["X","X","X","X","O"]
# ["X","O","X","O","X"] ["X","X","X","X","X"]
# ["O","X","O","O","O"] ["O","X","X","X","O"]
# ["X","X","O","X","O"] ["X","X","O","X","O"]


      
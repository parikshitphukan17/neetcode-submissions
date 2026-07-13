class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M,N = len(board),len(board[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def bfs(q):
            while q:
                child = deque([])
                while q:
                    i,j = q.popleft()
                    board[i][j] = "T"
                    for dx,dy in dir:
                        x = i+dx
                        y = j+dy
                        if x<0 or x==M or y<0 or y==N or board[x][y] != "O":
                            continue
                        child.append([x,y])
                q = child

        q = deque([])
        for i in range(M):
            if board[i][0] == "O":
                q.append([i,0])
            if board[i][N-1] == "O":
                q.append([i,N-1])
        for j in range(1,N-1):
            if board[0][j] == "O":
                q.append([0,j])
            if board[M-1][j] == "O":
                q.append([M-1,j])
        bfs(q)
        for i in range(M):
            for j in range(N):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        



        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh= 0
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        N,M = len(grid),len(grid[0])
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    q.append([i,j])
        if fresh == 0:
            return 0
        t = 0
        while q:
            nextQ = []
            while q:
                i,j = q.pop()
                if grid[i][j] == 1:
                    fresh -=1
                grid[i][j] = 2
                for dx,dy in dir:
                    nx,nj = dx+i,dy+j
                    if nx<0 or nj<0 or nx ==N or nj == M or grid[nx][nj] != 1:
                        continue
                    nextQ.append([nx,nj])
            if fresh == 0:
                return t
            t+=1
            q = nextQ
        return t if fresh == 0 else -1
                    


        
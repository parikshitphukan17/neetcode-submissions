class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        N,M = len(grid),len(grid[0])

        def bfs(q):
            t=0
            while q:
                child = []
                while q:
                    i,j = q.pop()
                    if i<0 or j<0 or i==N or j==M or grid[i][j] !=1:
                        continue
                    self.fresh -=1
                    grid[i][j] = 0
                    for dx,dy in dire:
                        child.append([i+dx,j+dy])
                q = child
                if self.fresh == 0:
                    return t
                t +=1
            return -1
        q = []
        self.fresh = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    grid[i][j] = 1
                    q.append([i,j])
                    self.fresh +=1
                elif grid[i][j] == 1:
                    self.fresh +=1
        return bfs(q) if self.fresh else 0


        
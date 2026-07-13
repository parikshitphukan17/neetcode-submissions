class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        N,M = len(grid),len(grid[0])
        self.t = 0
        self.fresh = 0
        def bfs(q):
            while q:
                child = []
                while q:
                    i,j = q.pop()
                    for dx,dy in dire:
                        x = i+dx
                        y = j+dy
                        if x<0 or y<0 or x==N or y==M or grid[x][y] !=1:
                            continue
                        grid[x][y] = 2
                        self.fresh -=1
                        child.append([x,y])
                if not child:
                    return
                q = child
                self.t +=1
        q =[]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    self.fresh +=1
        bfs(q)
        return self.t if self.fresh == 0 else -1
        

        
            



        
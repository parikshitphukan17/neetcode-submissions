class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N,M,fresh,q = len(grid),len(grid[0]),0,[]
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        vis = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    q.append([i,j])
        if fresh == 0:
            return 0
        t = -1
        while q:
            child = []
            while q:
                i,j = q.pop()
                for dx,dy in dire:
                    nx = i+dx
                    ny = j+dy
                    if nx <0 or nx == N or ny <0 or ny == M or (nx,ny) in vis or grid[nx][ny] != 1:
                        continue
                    vis.add((nx,ny))
                    child.append([nx,ny])
                    fresh -=1
            q = child
            t+=1
        return t if fresh == 0 else -1
                    
                    

        
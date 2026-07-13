class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        N,M = len(grid),len(grid[0])
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        def bfs(i,j):
            dist = 0
            q = [[i,j]]
            while q:
                child = []
                while q:
                    x,y  = q.pop()
                    if x<0 or y<0 or x == N or y == M or grid[x][y] < dist:
                        continue
                    grid[x][y] = dist
                    for dx,dy in dire:
                        child.append([x+dx,y+dy])
                dist +=1
                q = child
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    bfs(i,j)
        




        
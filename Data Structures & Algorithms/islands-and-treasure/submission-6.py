class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        vis = set()
        N,M= len(grid),len(grid[0])
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        q = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    q.append([i,j])
        dist = 0
        while q:
            nextQ = []
            while q:
                i,j = q.pop()
                if i<0 or j<0 or i==N or j==M or grid[i][j] == -1 or (i,j) in vis:
                    continue
                vis.add((i,j))
                grid[i][j] = dist
                for dx,dy in dir:
                    nextQ.append([i+dx,j+dy])
            q = nextQ
            dist +=1
        



        
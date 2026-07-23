class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        M,N = len(grid),len(grid[0])
        vis = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    q.append([i,j])
                    vis.add((i,j))
        dist = 0
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            nextQ = []
            while q:
                i,j = q.pop()
                grid[i][j] = dist
                for dx,dy in dir:
                    x,y = i+dx,j+dy
                    if x<0 or y<0 or x==M or y ==N or grid[x][y] != 2**31 -1 or (x,y) in vis:
                        continue
                    vis.add((x,y))
                    nextQ.append([x,y])
            q = nextQ
            dist +=1
        
                    


                
        
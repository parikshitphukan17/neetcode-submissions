class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dire = [[0,1],[0,-1],[1,0],[-1,0]]
        l,b = len(grid),len(grid[0])
        def dfs(i,j,vis,dist):
            if (i,j) in vis or i<0 or i==l or j<0 or j==b or grid[i][j] == -1 or (grid[i][j]!=0 and grid[i][j]<dist+1):
                return
            grid[i][j] = min(grid[i][j],dist+1)
            vis.add((i,j))
            for dx,dy in dire:
                dfs(i+dx,j+dy,vis,grid[i][j])
            vis.remove((i,j))
        for x in range(l):
            for y in range(b):
                if grid[x][y] == 0:
                    dfs(x,y,set(),0)
        

            

        
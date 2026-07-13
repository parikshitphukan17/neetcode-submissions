class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        l,b = len(grid),len(grid[0])
        def dfs(i,j,vis):
            if (i,j) in vis or i<0 or i==l or j<0 or j==b or grid[i][j] !="1":
                return
            grid[i][j] = "0"
            vis.add((i,j))
            for dx,dy in dire:
                dfs(i+dx,j+dy,vis)
        res = 0
        for x in range(l):
            for y in range(b):
                if grid[x][y] == "1":
                    res +=1
                    dfs(x,y,set())
        return res


            
            

        
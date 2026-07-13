class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[0,-1],[1,0],[-1,0]]
        l,b = len(grid),len(grid[0])
        def dfs(i,j):
            if i <0 or i == l or j<0 or j == b or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            area = 1
            for dx,dy in dire:
                area += dfs(i+dx,j+dy)
            return area
        res = 0
        for x in range(l):
            for y in range(b):
                if grid[x][y] == 1:
                    res = max(res,dfs(x,y))
        return res

        
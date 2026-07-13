class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[0,-1],[1,0],[-1,0]]
        l,b = len(grid),len(grid[0])
        def dfs(i,j,vis):
            if (i,j) in vis or i<0 or j<0 or i==l or j == b or grid[i][j]== 0:
                return
            vis.add((i,j))
            
            if grid[i][j] == 1:
                grid[i][j] = 2
                return
            for dx,dy in dire:
                dfs(i+dx,j+dy,vis)
        cur = set()
        sec = -1
        cnt =0
        for x in range(l):
            for y in range(b):
                if grid[x][y] == 2:
                    cnt +=1
        

        while True:
            cur = set()
            for x in range(l):
                for y in range(b):
                    if grid[x][y] == 2 and (x,y) not in cur:
                        dfs(x,y,cur)
            if cnt == len(cur):
                break
            sec +=1
            cnt = len(cur)
        for x in range(l):
            for y in range(b):
                if grid[x][y] == 1:
                    return -1
        return sec +1
            
            
            


        
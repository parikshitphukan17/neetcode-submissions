class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        N,M = len(grid),len(grid[0])
        def bfs(i,j):

            dist = 0
            q = [[i,j]]
            while q:
                child = []
                dist +=1
                while q:
                    curi,curj = q.pop()
                    for dx,dy in dire:
                        x = curi +dx
                        y = curj +dy
                        if x<0 or y<0 or x==N or y==M or grid[x][y]<dist:
                            continue
                        grid[x][y] = dist
                        child.append([x,y])
                q = child
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    bfs(i,j)
        


                    
                    

        
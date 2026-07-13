class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        N,M,dire= len(grid),len(grid[0]),[[0,1],[1,0],[0,-1],[-1,0]]
        
        def bfs(i,j):
            vis = set()
            q = [[i,j]]
            dist = 0
            while q:
                print(q,dist)
                children = []
                for qx,qy in q:
                    for dx,dy in dire:
                        grid[qx][qy] = min(grid[qx][qy],dist)
                        
                        X = qx+dx
                        Y = qy+dy
                        if X>=0 and X<N and Y>=0 and Y<M and (X,Y) not in vis and grid[X][Y] != -1:
                            children.append([X,Y])
                            vis.add((X,Y))
                q=children
                dist +=1
        
        for x in range(N):
            for y in range(M):
                if grid[x][y] == 0:
                    bfs(x,y)
                    print(grid)

                    

        
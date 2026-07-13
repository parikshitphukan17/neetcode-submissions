class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        N,M =len(grid),len(grid[0])
        def bfs(q):
            dire = [[0,1],[1,0],[0,-1],[-1,0]]
            path = 0
            vis = set()
            while q:
                child = []
                while q:
                    i,j = q.pop()
                    if i<0 or j<0 or i ==N or j ==M  or grid[i][j] == -1 or (i,j) in vis:
                        continue
                    vis.add((i,j))
                    grid[i][j] = path
                    for dx,dy in dire:
                        child.append([i+dx,j+dy])
                path +=1
                q = child
        q = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    q.append([i,j])
        bfs(q)
        





        
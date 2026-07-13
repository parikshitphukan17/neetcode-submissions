class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        heap = []
        M,N = len(grid),len(grid[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        vis = set()

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    heapq.heappush(heap,[0,i,j])
                    vis.add((i,j))
        while heap:
            val,i,j = heapq.heappop(heap)
            for dx,dy in dir:
                x=i+dx
                y=j+dy
                if x<0 or x==M or y<0 or y==N or (x,y) in vis or grid[x][y] == -1:
                    continue
                vis.add((x,y))
                grid[x][y] = val+1
                heapq.heappush(heap,[val+1,x,y])
        
            



            
        
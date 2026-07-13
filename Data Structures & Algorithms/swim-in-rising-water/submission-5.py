class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        N,M = len(grid),len(grid[0])
        heap = [[grid[0][0],0,0]]
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        res = 0
        vis = set()
        while heap:
            w,i,j = heapq.heappop(heap)
            res = max(res,grid[i][j])
            if i == N-1 and j ==M-1:
                return res
            for dx,dy in dir:
                x,y = i+dx,j+dy
                if (x,y) in vis or x<0 or y<0 or x==N or y ==M:
                    continue
                vis.add((x,y))
                heapq.heappush(heap,[grid[x][y],x,y])

            

        


        
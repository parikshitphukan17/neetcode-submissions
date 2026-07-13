import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        vis = set()
        vis.add((0,0))
        res = 0
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        heap = [[grid[0][0],0,0]]
        N,M = len(grid),len(grid[0])
        while heap:
            cur,i,j = heapq.heappop(heap)
            res = max(res,cur)
            if i==N-1 and j == M-1:
                return res
            for dx,dy in dir:
                x = i+dx
                y = j+dy
                if (x,y) in vis or x <0 or x == N or y<0 or y ==M:
                    continue
                vis.add((x,y))
                heapq.heappush(heap,[grid[x][y],x,y])
                

            
        
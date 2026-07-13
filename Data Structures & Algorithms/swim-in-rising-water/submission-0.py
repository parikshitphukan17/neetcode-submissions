import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        vis = set()
        heap = [[grid[0][0],0,0]]
        res = 0
        N,M = len(grid),len(grid[0])
        while heap:
            c,x,y = heapq.heappop(heap)
            vis.add((x,y))
            res = max(res,c)
            if x == N-1 and y == M-1:
                return res
            for dx,dy in dire:
                i,j = x+dx,y+dy
                if i>=0 and i<N and j>=0 and j<M and (i,j) not in vis:
                    heapq.heappush(heap,[grid[i][j],i,j])
        
                

        
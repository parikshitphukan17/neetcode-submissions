import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        heap = [[grid[0][0],0,0]]
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        N = len(grid)
        vis = set()
        while heap:
            w,i,j = heapq.heappop(heap)
            vis.add((i,j))
            res = max(res,w)
            if i==N-1 and j == N-1:
                return res
            for dx,dy in dire:
                x = i+dx
                y = j+dy
                if x>=0 and y>=0 and x<N and y<N and (x,y) not in vis:
                    heapq.heappush(heap,[grid[x][y],x,y])
        return res
        
            


        
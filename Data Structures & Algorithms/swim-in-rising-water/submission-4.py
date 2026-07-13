class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        heap = [[grid[0][0],0,0]]
        N,M = len(grid),len(grid[0])
        res = 0
        vis = set()
        vis.add((0,0))
        while heap:
            h,x,y = heapq.heappop(heap)
            res = max(res,h)
            if x==N-1 and y==M-1:
                return res
            for dx,dy in dire:
                nx,ny = dx+x,dy+y
                if nx<0 or nx==N or ny<0 or ny==M or (nx,ny) in vis:
                    continue
                vis.add((nx,ny))
                heapq.heappush(heap,[grid[nx][ny],nx,ny])

            






    

        
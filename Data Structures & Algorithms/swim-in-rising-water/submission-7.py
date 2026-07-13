class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [[grid[0][0],0,0]]
        res = 0
        M,N = len(grid),len(grid[0])
        vis = set()
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        vis.add((0,0))
        while heap:
            level,i,j = heapq.heappop(heap)
            res = max(res,level)
            if i == M-1 and j ==N-1:
                return res
            
            for dx,dy in dir:
                nx,ny = i+dx,j+dy
                if (nx,ny) in vis or nx<0 or nx ==M or ny<0 or ny ==N:
                    continue
                vis.add((nx,ny))
                heapq.heappush(heap,[grid[nx][ny],nx,ny])
        








        
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        res = -1
        heapq.heappush(heap,[grid[0][0],0,0])
        M,N = len(grid),len(grid[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        vis = set()
        vis.add((0,0))
        while True:
            water,i,j = heapq.heappop(heap)
            res = max(res,water)
            if i==M-1 and j==N-1:
                return res
            for dx,dy in dir:
                x,y = i+dx,j+dy
                if x<0 or y<0 or x==M or y ==N or (x,y) in vis:
                    continue
                vis.add((x,y))
                heapq.heappush(heap,[grid[x][y],x,y])
        
        
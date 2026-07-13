class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        q = deque([])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        fresh = 0
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh +=1
        if not fresh:
            return res
        while q:
            child = deque([])
            while q:
                i,j = q.popleft()
                if grid[i][j] == 1:
                    fresh -=1
                grid[i][j] = 2
                for dx,dy in dir:
                    x = i+dx
                    y = j+dy
                    if x<0 or x==M or y<0 or y ==N or grid[x][y] != 1:
                        continue
                    child.append([x,y])
            if fresh == 0:
                return res
            res +=1
            q = child
        return -1


                
                
                
        
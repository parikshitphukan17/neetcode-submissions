class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        fresh = 0
        q = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append([i,j])
                    grid[i][j] = 1
                    fresh +=1

                elif grid[i][j] == 1:
                    fresh +=1
        time = 0
        if fresh ==0:
            return time
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            nextQ = deque()
            while q:
                i,j = q.popleft()
                if i<0 or j<0 or i==M or j==N or grid[i][j] != 1:
                    continue
                grid[i][j] = 2
                fresh -=1
                for dx,dy in dir:
                    nextQ.append([i+dx,j+dy])
            time +=1
            if fresh == 0:
                return time-1
            q = nextQ
        return -1
                
                    


                
        
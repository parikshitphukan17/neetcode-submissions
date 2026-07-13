class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N,M,dire = len(grid),len(grid[0]),[[0,1],[1,0],[0,-1],[-1,0]]
        res = [-float("infinity")]
        def bfs(q):
            vis = set()
            t = 0
            while q:
                child =[]
                res[0] = max(res[0],t)
                for i,j in q:
                    grid[i][j] = 2
                    for dx,dy in dire:
                        cx,cy = i+dx,j+dy
                        if cx>=0 and cx<N and cy>=0 and cy<M and grid[cx][cy] == 1:
                            child.append([cx,cy])
                t+=1
                q = child
        def check():
            for i in range(N):
                for j in range(M):
                    if grid[i][j] == 1:
                        return [-1]
            return [max(res[0],0)]
        queue = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    queue.append([i,j])
        bfs(queue)
        val = check()[0]
        return val if val!=-float("infinity") else -1
            
        
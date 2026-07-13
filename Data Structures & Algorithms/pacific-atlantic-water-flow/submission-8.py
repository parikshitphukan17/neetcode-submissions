class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        N,M = len(heights),len(heights[0])
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        def bfs(src,canReach):
            q = src
            while q:
                child = []
                while q:
                    i,j = q.pop()
                    canReach.add((i,j))
                    for dx,dy in dire:
                        x = i+dx
                        y = j+dy
                        if x<0 or x == N or y<0 or y ==M or heights[x][y]<heights[i][j] or(x,y) in canReach:
                            continue
                        child.append([x,y])
                q = child
        
        atl,atlCanReach,pac,pacCanReach = [],set(),[],set()
        for j in range(M):
            atl.append([N-1,j])
            pac.append([0,j])
        for i in range(N):
            pac.append([i,0])
            atl.append([i,M-1])
        
        bfs(atl,atlCanReach)
        bfs(pac,pacCanReach)
        res = []
        for i in range(N):
            for j in range(M):
                if (i,j) in atlCanReach and (i,j) in pacCanReach:
                    res.append([i,j])
        return res




        
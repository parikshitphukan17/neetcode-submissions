class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        N,M =len(heights),len(heights[0])
        for i in range(N):
            pac.add((i,0))
            atl.add((i,M-1))
        for j in range(M):
            pac.add((0,j))
            atl.add((N-1,j))
        def bfs(ocean,vis):
            q = []
            for i,j in ocean:
                q.append([i,j])
                vis.add((i,j))
            while q:
                nextQ = []
                while q:
                    i,j = q.pop()
                    ocean.add((i,j))
                    for dx,dy in dir:
                        nx,ny = i+dx,j+dy
                        if nx<0 or ny<0 or nx ==N or ny == M or heights[nx][ny]<heights[i][j] or (nx,ny) in vis:
                            continue
                        vis.add((nx,ny))
                        nextQ.append([nx,ny])
                q = nextQ
        bfs(pac,set())
        bfs(atl,set())
        res = []
        for i in range(N):
            for j in range(M):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])  
        return res                          
                            

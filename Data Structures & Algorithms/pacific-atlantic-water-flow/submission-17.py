class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac = set()
        atl = set()
        M,N = len(heights),len(heights[0])
        for i in range(M):
            pac.add((i,0))
            atl.add((i,N-1))
        for j in range(N):
            pac.add((0,j))
            atl.add((M-1,j))
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        def fill(ocean):
            vis = set()
            q = deque()
            for i,j in ocean:
                q.append([i,j])
                vis.add((i,j))
            while q:
                nextQ = deque()
                while q:
                    i,j = q.popleft()
                    ocean.add((i,j))
                    for dx,dy in dir:
                        x,y = i+dx,j+dy
                        if x<0 or y<0 or x==M or y ==N or (x,y) in vis or heights[x][y]<heights[i][j]:
                            continue
                        nextQ.append([x,y])
                        vis.add((x,y))
                q = nextQ
        
        fill(pac)
        fill(atl)
        res = []
        for i in range(M):
            for j in range(N):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res

            
                        


        
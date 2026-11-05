class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        M,N = len(heights), len(heights[0])
        for i in range(M):
            for j in range(N):
                if i==0 or j==0:
                    pac.add((i,j))
                    
                if i==M-1 or j==N-1:
                    atl.add((i,j))
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def fill(ocean):
            vis = set()
            q = deque(list(ocean))
            while q:
                i,j = q.popleft()
                if (i,j) in vis:
                    continue
                vis.add((i,j))
                ocean.add((i,j))
                for dx,dy in dir:
                    x,y = i+dx,j+dy
                    if x<0 or y<0 or x==M or y==N or heights[x][y]<heights[i][j]:
                        continue
                    q.append([x,y])
        fill(pac)
        fill(atl)
        res = []
        for i in range(M):
            for j in range(N):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res


            


        
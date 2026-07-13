class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M,N = len(heights),len(heights[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def fill(ocean):
            vis = set()
            stack = deque([])
            for i,j in ocean:
                stack.append([i,j])
                vis.add((i,j))
            while stack:
                i,j = stack.popleft()
                for dx,dy in dir:
                    x = i+dx
                    y = j+dy
                    if x<0 or x==M or y<0 or y==N or heights[x][y]<heights[i][j] or (x,y) in vis:
                        continue
                    vis.add((x,y))
                    ocean.add((x,y))
                    stack.append((x,y))
        pac = set()
        atl = set()
        for i in range(M):
            pac.add((i,0))
            atl.add((i,N-1))
        
        for j in range(N):
            pac.add((0,j))
            atl.add((M-1,j))
        fill(pac)
        fill(atl)
        res = []
        for i in range(M):
            for j in range(N):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res







            
            

                    


        
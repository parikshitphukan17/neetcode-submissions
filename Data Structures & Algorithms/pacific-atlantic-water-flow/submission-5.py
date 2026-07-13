class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac,atl = set(),set()
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        N,M = len(heights),len(heights[0])
        for i in range(N):
            pac.add((i,0))
            atl.add((i,M-1))
        for j in range(M):
            pac.add((0,j))
            atl.add((N-1,j))
        vis = set()
        def dfs(i,j,reached):
            if (i,j) in reached:
                return True
            canReach = False
            for dx,dy in dire:
                x,y = i+dx,j+dy
                if(x>=0 and y>=0 and x<N and y<M and (x,y) not in vis and heights[x][y]<= heights[i][j]):
                    vis.add((x,y))
                    canReachNext = dfs(x,y,reached)
                    vis.remove((x,y))
                    if canReachNext:
                        canReach = True
            if canReach:
                reached.add((i,j))
            return canReach
        for i in range(N):
            for j in range(M):
                vis = set()
                dfs(i,j,pac)
        res = []
        for x,y in pac:
            vis = set()
            if dfs(x,y,atl):
                res.append([x,y])
        return res



                


        
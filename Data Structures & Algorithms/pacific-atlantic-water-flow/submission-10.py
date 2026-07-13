class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        N,M = len(heights),len(heights[0])
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        pac,pacQ,atl,atlQ = set(),[],set(),[]
        for i in range(N):
            pacQ.append([i,0])
            atlQ.append([i,M-1])
        
        for j in range(M):
            pacQ.append([0,j])
            atlQ.append([N-1,j])

        def bfs(q,canReach):
            while q:
                i,j = q.pop()
                canReach.add((i,j))
                for dx,dy in dir:
                    x = i+dx
                    y = j+dy
                    if x<0 or x ==N or y<0 or y == M or heights[x][y] < heights[i][j] or (x,y) in canReach:
                        continue
                    q.append([x,y])
        
        bfs(atlQ,atl)
        bfs(pacQ,pac)
        res = []
        for i in range(N):
            for j in range(M):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])
        return res

            


        
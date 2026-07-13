class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        vis = set()
        N,M = len(matrix),len(matrix[0])
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(i,j):
            vis.add((i,j))
            path = 0
            q = [[i,j]]
            while q:
                path += 1
                child = []
                while q:
                    x,y = q.pop()
                    for dx,dy in dire:
                        X = x+dx
                        Y = y+dy
                        if X>=0 and X<N and Y>=0 and Y<M and matrix[X][Y]>matrix[x][y]:
                            child.append([X,Y])
                            vis.add((X,Y))
                q = child
            return path
        res = 0
        for i in range(N):
            for j in range(M):
                if (i,j) not in vis:
                    res = max(res,bfs(i,j))
        return res

        
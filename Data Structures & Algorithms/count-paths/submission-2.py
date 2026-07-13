class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path =[0]*(n+1)
        path[n-1] = 1
        for i in range(m-1,-1,-1):
            newPath = [0]*(n+1)
            for j in range(n-1,-1,-1):
                newPath[j] += path[j]+newPath[j+1]
            path = newPath
        return path[0]
        
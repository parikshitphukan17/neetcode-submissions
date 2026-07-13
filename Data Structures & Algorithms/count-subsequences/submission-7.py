class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N,M = len(s),len(t)
        dp = {}
        def dfs(i,j):
            if j == M:
                return 1
            if i == N:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1,j) + dfs(i+1,j+1)
            else:
                dp[(i,j)] = dfs(i+1,j)
            return dp[(i,j)]
        return dfs(0,0)
        
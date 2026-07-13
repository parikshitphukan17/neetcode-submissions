class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N,M = len(s),len(t)
        def dfs(i,j):
            if j == M:
                return 1
            if i == N:
                return 0
            if s[i] == t[j]:
                return dfs(i+1,j+1) + dfs(i+1,j)
            else:
                return dfs(i+1,j)
        return dfs(0,0)


        
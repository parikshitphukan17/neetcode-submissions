class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N,M = len(s),len(t)
        dp = [0]*(M+1)
        dp[M] = 1
        
        for i in range(N-1,-1,-1):
            cur = [0]*(M+1)
            cur[M] = 1
            for j in range(M-1,-1,-1):
                cur[j] = dp[j]
                if s[i] == t[j]:
                    cur[j] += dp[j+1]
            dp = cur
        return dp[0]

        # def dfs(i,j):
        #     if j == M:
        #         return 1
        #     if i == N:
        #         return 0
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     dp[(i,j)] = dfs(i+1,j)
        #     if s[i] == t[j]:
        #         dp[(i,j)] += dfs(i+1,j+1)
        #     return dp[(i,j)]
        # return dfs(0,0)


        
        # caaat
        # i
        # cat
        # j
        # if i== j
        # i+1,j+1 + i+1,j
        # if i!=j
        # i+1
        # j
        
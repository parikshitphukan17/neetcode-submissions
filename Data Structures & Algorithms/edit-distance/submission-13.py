class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M,N = len(word1),len(word2)
        dp = [0]*(N+1)
        for i in range(M,-1,-1):
            cur = [0]*(N+1)
            for j in range(N,-1,-1):
                if i ==M:
                    cur[j] = N-j
                elif j ==N:
                    cur[j] = M-i
                elif word1[i] == word2[j]:
                    cur[j] = dp[j+1]
                else:
                    cur[j] = 1 + min(cur[j+1],dp[j],dp[j+1])
            dp = cur
        return dp[0]

        # def dfs(i,j):
        #     if i == M:
        #         return N-j
        #     if j==N:
        #         return M-i
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if word1[i] == word2[j]:
        #         dp[(i,j)] = dfs(i+1,j+1)
        #     else:
        #         dp[(i,j)] = 1+ min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1))
        #     return dp[(i,j)]
        # return dfs(0,0)


        # 1   2   3   4   5   6   7   8
        # m   o   n   k   e   y   s
        # m   o   n   e   y
        # if i ==m:
        #     if j==n:
        #         return 0
        #     return n-m
        # if j==n:
        #     return m-n

            

        # if i==j:
        #     return dfs(i+1,j+1)
        # else:
        #     1+min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1))
        
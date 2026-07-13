class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        M,N = len(word1),len(word2)
        def dfs(i,j):
            if i == M:
                return N-j
            if j==N:
                return M-i
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1,j+1)
            else:
                dp[(i,j)] = 1+ min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1))
            return dp[(i,j)]
        return dfs(0,0)


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
        
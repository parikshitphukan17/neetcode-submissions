class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        N,M = len(text1),len(text2)
        def dfs(i,j):
            if i == N or j == M:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            if text1[i] == text2[j]:
                dp[(i,j)] = 1 + dfs(i+1,j+1)
            else:
                dp[(i,j)] = max(dfs(i,j+1),dfs(i+1,j))
            return dp[(i,j)]
        return dfs(0,0)


        
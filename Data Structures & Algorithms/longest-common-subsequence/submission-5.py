class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i,j = 0,0
        dp = [0]*(len(text2)+1)
        for i in range(len(text1)-1,-1,-1):
            newRow = [0]*(len(text2)+1)
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    newRow[j] = 1 +dp[j+1]
                else:
                    newRow[j] = max(newRow[j+1],dp[j])
            dp = newRow
        return dp[0]

        # def dfs(i,j):
        #     if i == len(text1):
        #         return 0
        #     if j == len(text2):
        #         return 0
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if text1[i] == text2[j]:
        #         dp[(i,j)] = 1 + dfs(i+1,j+1)
        #     else:
        #         dp[(i,j)] = max(dfs(i,j+1),dfs(i+1,j))
        #     return dp[(i,j)]
        # return dfs(0,0)
        
        
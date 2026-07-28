class Solution:
    def canPartition(self, nums: List[int]) -> bool:


        N = len(nums)
        s = sum(nums)
        if s%2 != 0:
            return False
        half = s//2
        dp = [[False]*(half+1) for _ in range(N+1)]
        for i in range(N):
            dp[i][half] = True
        for i in range(N-1,-1,-1):
            for j in range(half-1,-1,-1):
                if j+nums[i]<=half:
                    dp[i][j] |= dp[i+1][j+nums[i]] or dp[i+1][j]
                else:
                    dp[i][j] |= dp[i+1][j]
        return dp[0][0]


        # 

        # def dfs(i,cur):
        #     if (i,cur) in dp:
        #         return dp[(i,cur)]
        #     if cur == half:
        #         dp[(i,cur)] = True
        #         return True
        #     if cur>half or i == N:
        #         dp[(i,cur)] = False
        #         return False
            
        #     dp[(i,cur)] = dfs(i+1,cur+nums[i]) or dfs(i+1,cur)
        #     return dp[(i,cur)]
        # return dfs(0,0)
        



        
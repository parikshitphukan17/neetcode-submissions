class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        L = len(nums)
        if s%2 != 0 :
            return False
        mid = s//2
        dp = {}
        def dfs(i,sm):
            print(i,sm,dp)
            if (i,sm) in dp:
                return dp[i]
            if sm == mid:
                dp[i] = True
            elif sm >mid or i == L:
                dp[i] = False
            else:
                dp[i] = dfs(i+1,sm) or dfs(i+1,sm+nums[i])
            return dp[i]
        return dfs(0,0)
        
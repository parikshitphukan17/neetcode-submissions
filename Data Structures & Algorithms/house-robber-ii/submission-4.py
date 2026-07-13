class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = {}
        def dfs(i,nums):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            dp[i]  =max(nums[i] + dfs(i+2,nums),dfs(i+1,nums))
            return dp[i]
        res = dfs(0,nums[:len(nums)-1])
        dp = {}
        return max(res,dfs(0,nums[1:]))
        
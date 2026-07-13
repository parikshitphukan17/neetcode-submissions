class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        N = len(nums)
        def dfs(i,sm):
            if i == N:
                return 1 if sm == target else 0
            if (i,sm) in dp:
                return dp[(i,sm)]
            
            dp[(i,sm)] = dfs(i+1,sm+nums[i]) + dfs(i+1,sm-nums[i])
            return dp[(i,sm)]
        return dfs(0,0)

        
        
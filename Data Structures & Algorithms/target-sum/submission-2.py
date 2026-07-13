class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i,sm):
            if i==len(nums):
                return sm == target
            return dfs(i+1,sm-nums[i]) + dfs(i+1,sm+nums[i])
        return dfs(0,0)
        
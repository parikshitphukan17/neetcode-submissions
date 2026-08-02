class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        N = len(nums)
        def dfs(i,cur):
            if i==N:
                return 1 if cur == target else 0
            if (i,cur) in dp:
                return dp[(i,cur)]
            dp[(i,cur)] = dfs(i+1,cur+nums[i]) + dfs(i+1,cur-nums[i])
            return dp[(i,cur)]
        return dfs(0,0)
        
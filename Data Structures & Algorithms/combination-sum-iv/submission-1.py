class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(s):
            if s>target:
                return 0
            if s==target:
                return 1
            if s in dp:
                return dp[s]
            res = 0
            for n in nums:
                res+=dfs(s+n)
            dp[s] = res
            return dp[s]
        return dfs(0)

            
        
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        def dfs(l,r):
            if l>=r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l+1,r):
                dp[(l,r)] = max(dp[(l,r)],nums[l]*nums[r]*nums[i]+dfs(l,i)+dfs(i,r))
            return dp[(l,r)]
        nums = [1]+nums+[1]
        return dfs(0,len(nums)-1)
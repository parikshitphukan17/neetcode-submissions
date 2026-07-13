class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        def dfs(nums):
            if len(nums) ==3:
                return nums[1]
            res = 0
            for i in range(1,len(nums)-1):
                res = max(res,nums[i-1]*nums[i]*nums[i+1] + dfs(nums[:i]+nums[i+1:]))
            return res
        return dfs(nums)

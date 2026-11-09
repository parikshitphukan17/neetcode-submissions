class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = nums[-1]
        dp2 = 0
        for i in range(N-2,-1,-1):
            cur = max(nums[i]+dp2,dp)
            dp2 = dp
            dp = cur
        return dp

        
        
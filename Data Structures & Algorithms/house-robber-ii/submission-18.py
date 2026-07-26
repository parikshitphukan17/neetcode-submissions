class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            if not nums:
                return -1
            N = len(nums)+1
            sum2 = 0
            sum1 = nums[-1]
            for i in range(N-3,-1,-1):
                cur = max(nums[i]+sum2,sum1)
                sum2 = sum1
                sum1 = cur
            return sum1
        
        return max(helper(nums[1:]),helper(nums[:len(nums)-1]))

        

        
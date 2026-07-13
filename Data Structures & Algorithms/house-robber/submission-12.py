class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        N = len(nums)
        a = nums[N-1]
        b = 0
        cur = 0
        for i in range(N-2,-1,-1):
            cur = max(b+nums[i],a)
            b = a
            a = cur
            
        return cur
        
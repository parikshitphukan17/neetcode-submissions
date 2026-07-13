class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        res = -1001
        for i in nums:
            cur = prev + i
            res = max(res,cur)
            prev = max(0,cur)
        return res

        
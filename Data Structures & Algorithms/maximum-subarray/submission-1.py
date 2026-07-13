class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        last = 0
        res = -1001
        for i in nums:
            s = last+i
            res = max(res,s)
            last = max(s,0)
        return res



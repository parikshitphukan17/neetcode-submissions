class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = -1001
        cur = 0
        for n in nums:
            cur += n
            s = max(cur,s)
            cur = max(0,cur)
        return s



        
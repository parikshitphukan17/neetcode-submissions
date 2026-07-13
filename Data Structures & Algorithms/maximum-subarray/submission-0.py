class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        s = -1001
        cur = 0
        for i in nums:
            if prev+i>i:
                cur = prev+i
            else:
                cur = i
            s = max(s,cur)

            prev = cur
        return s

        
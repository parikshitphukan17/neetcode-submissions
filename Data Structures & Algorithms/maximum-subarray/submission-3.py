class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = -1001
        for i in nums:
            s = max(i,s+i)
            res = max(res,s)
        return res



# 0   [2,-3,4,-2,2,1,-1,4]
#      2, 0 4. 2.4.5  4  8
#     s = max(s+i,i)        
        
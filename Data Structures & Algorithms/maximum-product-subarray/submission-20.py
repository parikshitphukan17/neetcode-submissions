class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos,neg = 1,1
        res = -11
        for i in nums:
            npos = max(pos*i,neg*i)
            nneg = min(pos*i,neg*i)
            res = max(res,npos,nneg)
            pos = max(1,npos,nneg)
            neg = min(1,npos,nneg)
        return res




    #     2   4   -3  5   6   -3  
    # +   2   8   1   5   30  540
    # -   1   1   -24 -120 -180 -90    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg,pos = 1,1
        res = nums[0]
        for i in nums:
            nneg = min(neg*i,pos*i,i)
            npos = max(neg*i,pos*i,i)
            res = max(res,npos)
            neg,pos = nneg,npos
        return res






#         [1,2,-3,4,-5,-6]
# neg.1    1 1 -6 -24 -20  -6  
# pos 1    1 2  1 4   110  120
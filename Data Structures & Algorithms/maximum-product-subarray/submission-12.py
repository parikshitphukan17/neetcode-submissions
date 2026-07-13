class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg,pos = 1,1
        res = nums[0]
        for i in nums:
            nneg = min(i,neg*i,pos*i)
            npos = max(i,neg*i,pos*i)
            res = max(res,npos)
            neg,pos = nneg,npos
        return res
            
        




#         [1,2,-3,5,-2,5,-4]
# pos = 1  1 2 1  5 60
# neg = 1. 1 1 -6-30-10






#         [1,2,-3,4,-5,-6]
# neg.1    1 1 -6 -24 -20  -6  
# pos 1    1 2  1 4   110  120
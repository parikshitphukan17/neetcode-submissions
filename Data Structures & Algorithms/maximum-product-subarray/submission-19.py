class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMin,prevMax = 1,1
        res = -11
        for n in nums:
            res = max(res,n*prevMin,n*prevMax)
            nextMax = max(1,n*prevMin,n*prevMax)
            nextMin = min(1,n*prevMin,n*prevMax)
            prevMin,prevMax =nextMin, nextMax
        return res




#         2   4   -3  5   -4  5
# min 1   1   1   -24 -124 -20 -120 
# max 1   2   8    1  5   496
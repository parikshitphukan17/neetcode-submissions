class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMin,prevMax = 1,1
        res = -11
        for i in nums:
            res = max(i*prevMin,i*prevMax,res)
            nextMin = min(1,i*prevMin,i*prevMax)
            nextMax = max(1,i*prevMin,i*prevMax)
            prevMin,prevMax=nextMin,nextMax
        return res

# min 1   1   1   -6  -24 1
# *prevmin1   2   -3  -24 24 
#         1   2   -3  4   -1
# *prevmax1   2   -6  4   -4      
# max 1   1   2   1   4   24  




# do prevMin*i and prevMax*i and check for max for res
# calc nextMin = min(1,prevMin*i)
# calc nextMax = max(1,prevMax*i)
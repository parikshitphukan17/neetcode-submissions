class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        maxNegValue,maxPosValue = 0,0
        res = -11
        for i in nums:
            nextPos = max(maxNegValue * i,maxPosValue *i,i)
            nextNeg = min(maxNegValue * i,maxPosValue *i,i)
            maxNegValue =nextNeg
            maxPosValue = nextPos
            res = max(maxNegValue,maxPosValue,res)
        return res
            #if pos:
            #if last is negarive

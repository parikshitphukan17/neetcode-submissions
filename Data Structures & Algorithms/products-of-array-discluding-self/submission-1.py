class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prev = 1
        for n in nums:
            res.append(prev)
            prev*= n
        next = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*next
            next *= nums[i]
        return res






        





         
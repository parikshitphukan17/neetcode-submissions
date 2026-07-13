class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in numSet:
            if i-1 in numSet:
                continue
            conseC =1
            j=i
            while j+1 in numSet:
                conseC +=1
                j +=1
            res = max(res,conseC)
        return res 


        
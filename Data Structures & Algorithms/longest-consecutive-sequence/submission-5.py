class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        res = 0
        for n in nums:
            if n-1 in numSet:
                continue
            i = n
            len = 1
            while i+1 in numSet:
                i+=1
                len+=1
            res = max(res,len)
        return res
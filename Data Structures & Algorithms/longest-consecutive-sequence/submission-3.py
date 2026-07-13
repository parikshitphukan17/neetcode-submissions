class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in numSet:
            if i-1 in numSet:
                continue
            j = i
            cnt = 0
            while j in numSet:
                cnt +=1
                j+=1
            res = max(res,cnt)
        return res
            
        
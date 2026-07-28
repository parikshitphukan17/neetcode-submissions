from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [nums[0]]
        for i in range(1,N):
            if nums[i]>dp[-1]:
                dp.append(nums[i])
                continue
            idx = bisect_left(dp,nums[i])
            dp[idx] = nums[i]
        return len(dp)



       

        


        
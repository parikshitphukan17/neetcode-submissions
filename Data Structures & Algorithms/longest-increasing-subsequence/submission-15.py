class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        def dfs(i,j):
            if i == N:
                return 0
            LIS = dfs(i+1,j)
            if j == -1 or nums[i]>nums[j]:
                LIS = max(LIS,1+dfs(i+1,i))
            return LIS
        return dfs(0,-1)
            
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}
        def dfs(i,j):
            if i ==N:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            LIS = dfs(i+1,j)
            if j == -1 or nums[i]>nums[j]:
                LIS =  max(1+dfs(i+1,i),LIS)
            dp[(i,j)] = LIS
            return LIS
        return dfs(0,-1)





    #     9   1   4   2   3   3   7

    # -1001.  1   4   
    #     1   1   2
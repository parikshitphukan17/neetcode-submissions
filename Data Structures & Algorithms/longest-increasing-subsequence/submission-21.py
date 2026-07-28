class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}
        def dfs(prev,i):
            if (prev,i) in dp:
                return dp[(prev,i)]
            if i>=N:
                return 0
            if prev>=nums[i]:
                dp[(prev,i)] =  dfs(prev,i+1)
            else:
                dp[(prev,i)] =  max(1+dfs(nums[i],i+1),dfs(prev,i+1))
            return dp[(prev,i)]
        return dfs(-1001,0)


        


        
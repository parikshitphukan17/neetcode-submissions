class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2:
            return False
        req = s//2
        N = len(nums)
        dp = {}
        def dfs(i,s):
            if s>req or i== N:
                return False
            if (i,s) in dp:
                return dp[(i,s)]
            if s == req:
                return True
            dp[(i,s)] = dfs(i+1,s+nums[i]) or dfs(i+1,s)
            return dp[(i,s)]
        return dfs(0,0)
            




        



        
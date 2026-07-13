class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        L = len(nums)
        if s%2 != 0 :
            return False
        mid = s//2
        dp = {}
        def dfs(i,sm):
            print(i,sm,dp)
            if (i,sm) in dp:
                return dp[(i,sm)]
            if sm == mid:
                dp[(i,sm)] = True
            elif sm >mid or i == L:
                dp[(i,sm)] = False
            else:
                dp[(i,sm)] = dfs(i+1,sm) or dfs(i+1,sm+nums[i])
            return dp[(i,sm)]
        return dfs(0,0)
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2:
            return False
        half = s//2
        N = len(nums)
        dp = {}
        def dfs(i,cur):
            if cur == half:
                return True
            if cur>half or i==N:
                return False
            if (i,cur) in dp:
                return dp[(i,cur)]
            dp[(i,cur)] = dfs(i+1,cur+nums[i]) or dfs(i+1,cur)
            return dp[(i,cur)]
        return dfs(0,0)

         
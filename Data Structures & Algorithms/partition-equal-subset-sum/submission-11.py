class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)
        if s%2:
            return False
        half = s//2
        N = len(nums)
        dp = {}

        def dfs(i,cur):
            print(i,cur)
            if (i,cur) in dp:
                return dp[(i,cur)]
            if cur == half:
                dp[(i,cur)] = True
                return True
            if cur>half or i == N:
                dp[(i,cur)] = False
                return False
            
            dp[(i,cur)] = dfs(i+1,cur+nums[i]) or dfs(i+1,cur)
            return dp[(i,cur)]
        return dfs(0,0)
        



        
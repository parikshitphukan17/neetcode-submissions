class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2:
            return False
        req = s//2
        N = len(nums)
        dp = [False]*(req+1)
        dp[req] = True
        for i in range(N-1,-1,-1):
            cur = [False]*(req+1)
            cur[req] = True
            for j in range(req-1,-1,-1):
                if cur[j]:
                    continue
                cur[j] = dp[j] or (dp[j+nums[i]] if j+nums[i]<= req else False)
            dp = cur
        return dp[0]

        # def dfs(i,s):
        #     if s>req or i== N:
        #         return False
        #     if (i,s) in dp:
        #         return dp[(i,s)]
        #     if s == req:
        #         return True
        #     dp[(i,s)] = dfs(i+1,s+nums[i]) or dfs(i+1,s)
        #     return dp[(i,s)]
        # return dfs(0,0)
            




        



        
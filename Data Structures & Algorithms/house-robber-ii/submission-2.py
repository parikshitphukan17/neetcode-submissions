class Solution:
    def rob(self, nums: List[int]) -> int:


        if len(nums)<=2:
            return max(nums)
        N = len(nums)
        c1,c2,cur = 0,0,0
        c3,c4,cur2 = 0,0,0
        for i in range(N-1,-1,-1):
            if i>=1:
                cur = max(nums[i]+c2,c1)
                c2 = c1
                c1 = cur
            if i<=N-2:
                cur2 = max(nums[i]+c4,c3)
                c4 = c3
                c3 = cur2
            
        return max(cur,cur2)




        # dp = {}
        # def dfs(n):
        #     if n>=N:
        #         return 0
        #     if n in dp:
        #         return dp[n]
        #     dp[n] = max(nums[n]+dfs(n+2),nums[n+1] +dfs(n+3) if n+1<N else 0)
        #     return dp[n]
        # val1 = dfs(1)
        # N -=1
        # dp = {}
        # val2 = dfs(0)
        # return max(val1,val2)
        
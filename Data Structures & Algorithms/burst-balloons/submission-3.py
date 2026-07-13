class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l,r):
            if l==r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            s = 0
            for i in range(l+1,r):
                cur = nums[l] *nums[i] * nums[r] +dfs(l,i) + dfs(i,r)
                s = max(cur,s)
            dp[(l,r)] = s
            return s
        return dfs(0,len(nums)-1)


        


        
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1]+nums+[1]
        def dfs(l,r):
            if r-l == 1:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l+1,r):
                dp[(l,r)] = max(dp[(l,r)],nums[l]*nums[r]*nums[i] + dfs(l,i)+ dfs(i,r))
            return dp[(l,r)]
        return dfs(0,len(nums)-1)

# l           r
# [1,4,2,3,7,1]

# 1*7*1 + dfs(1,4,2,3,7) + dfs(7,1)

# 1*4*7+ dfs(4,2,3,7)
# 4*3*7 + dfs(4,2,3)
# 4*2*3 + dfs(4,2) + dfs(2,3)





        
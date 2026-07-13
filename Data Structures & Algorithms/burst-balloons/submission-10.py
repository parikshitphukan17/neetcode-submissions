class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l,r):
            if (l,r) in dp:
                return dp[(l,r)]

            if r -l <=1:
                return 0
            dp[(l,r)] = 0
            for i in range(l+1,r):
                cur = nums[l]*nums[i]*nums[r]
                dp[(l,r)] = max(dp[(l,r)],cur+dfs(l,i)+dfs(i,r))
            return dp[(l,r)]
        return dfs(0,len(nums)-1)
    
    
# [1,4,2,3,7,1]


# 1*7*1 + dfs(0,4) + dfs(4,5) 
# 1*4*7 + dfs(0,1) + dfs(1,4)

# 4*3*7 + dfs(1,3) + dfs(3,4)
# 4*2*3 + dfs(1,2) + dfs(2,3)

        
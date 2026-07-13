class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        dp = {}
        def dfs(i,j):
            if i+1==j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res = 0
            for c in range(i+1,j,1):
                cur = nums[i]*nums[c]*nums[j] + dfs(i,c) + dfs(c,j)
                res = max(res,cur)
            dp[(i,j)] =  res
            return dp[(i,j)]
        return dfs(0,len(nums)-1)




        # [1,4,2,3,7,1]

        # 7+ [1,4,2,3,7] + [7,1]
        # 7+28+ [1,4]+[4,2,3,7]
        # 35+ 84+ [4,2,3] [3,7]
                
        
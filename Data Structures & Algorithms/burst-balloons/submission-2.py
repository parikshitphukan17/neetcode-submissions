class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                dp[(l,r)]
            res = 0
            for i in range(l,r+1):
                res = max(res,nums[l-1]*nums[i]*nums[r+1] +dfs(l,i-1)+dfs(i+1,r))
            dp[(l,r)] = res
            return dp[(l,r)]
        return dfs(1,len(nums)-2)


            

        # def dfs(nums):
        #     if len(nums) ==3:
        #         return nums[1]
        #     res = 0
        #     for i in range(1,len(nums)-1):
        #         res = max(res,nums[i-1]*nums[i]*nums[i+1] + dfs(nums[:i]+nums[i+1:]))
        #     return res
        # return dfs(nums)

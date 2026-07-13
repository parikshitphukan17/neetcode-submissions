class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l,r):
            if (l,r) in dp:
                return dp[(l,r)]
            if l>=r:
                return 0
            coins = 0
            for i in range(l+1,r):
                amt = nums[l] * nums[i] *nums[r]
                amt += dfs(l,i) + dfs(i,r)
                coins = max(coins,amt)
            dp[(l,r)] =  coins
            return dp[(l,r)]
        return dfs(0,len(nums)-1)


        
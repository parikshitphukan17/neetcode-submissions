class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = defaultdict(int)
        dp[target] = 1
        s = sum(nums)
        for i in range(N-1,-1,-1):
            row = defaultdict(int)
            for cur in range(s,-(s+1),-1):
                row[cur] = dp[cur+nums[i]] + dp[cur-nums[i]]
            dp = row
        return dp[0]
        # def dfs(i,cur):
        #     if i == N:
        #         return 1 if cur == target else 0
        #     if (i,cur) in dp:
        #         return dp[(i,cur)]
        #     dp[(i,cur)] = dfs(i+1,cur+nums[i]) + dfs(i+1,cur-nums[i])
        #     return dp[(i,cur)]
        # return dfs(0,0)




#         2   2   2   target = 2
#                                                         0,0
#                                     2,1                                     -2,1
#             4,2(1)                          0,2(1)                  0,2(1)          -4,2
# 6,3                 2,3                 2,3         -2,3
# 0                    1
        
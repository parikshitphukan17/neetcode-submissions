class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        cache ={}
        def dfs(n):
            if n>=N:
                return 0
            if n in cache:
                return cache[n]
            cache[n] = cost[n] + min(dfs(n+1),dfs(n+2))
            return cache[n]
        return min(dfs(0),dfs(1)) if N>=2 else dfs(0)
        
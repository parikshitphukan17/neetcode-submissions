class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(cur):
            if cur == n:
                return 1
            if cur>n:
                return 0
            return dfs(cur+1) + dfs(cur+2)
        return dfs(0)


        
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(cur):
            if cur == n:
                return 1
            if cur>n:
                return 0
            return climb(cur+1) + climb(cur+2)
        return climb(0)

        
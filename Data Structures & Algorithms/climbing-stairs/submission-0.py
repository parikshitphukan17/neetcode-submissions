class Solution:
    def climbStairs(self, n: int) -> int:
        climb = [0] *(n+1)
        climb[1] = 1
        climb[0] = 1
        for i in range(2,n+1,1):
            climb[i] = climb[i-1] + climb[i-2]
        return climb[n]
               

        
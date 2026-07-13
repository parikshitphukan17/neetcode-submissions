class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0]*4
        s = sum(matchsticks)
        if s % 4:
            return False
        req = s//4
        N = len(matchsticks)
        dp = {}
        def dfs(i):
            state = (i, tuple(sides))
            if state in dp:
                return dp[state]
            if i == N:
                return all(side==req for side in sides)
            for j in range(4):
                if sides[j] + matchsticks[i] <=req:
                    sides[j] += matchsticks[i] 
                    if dfs(i+1):
                        dp[state] =  True
                        return True
                    sides[j] -= matchsticks[i] 
            dp[state] =  False
            return dp[state]
        return dfs(0)
                    



#         1 3 4   2   2   4


#         1   4   2   4   2   3

#         /
#        1. 

#        1 + 4 = 5 X
#        1 +2 = 3 correct
#        3+4 = 7 X
#        3+2 = 5 X
#        3+3 = 6 X

#        1 + 3 = correct
# ans (0,5)


        





        
        
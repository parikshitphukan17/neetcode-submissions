class Solution:
    def checkValidString(self, s: str) -> bool:
        minBracks,maxBracks = 0,0
        for i in s:

            if i == "(":
                minBracks,maxBracks =minBracks+1, maxBracks+1
            elif i == ")":
                minBracks,maxBracks =minBracks-1, maxBracks-1
            else:
                minBracks,maxBracks = minBracks-1,maxBracks+1
            if maxBracks<0:
                return False
            
            minBracks = max(minBracks,0)
        return minBracks == 0 or maxBracks == 0


        
        
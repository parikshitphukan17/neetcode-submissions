class Solution:
    def checkValidString(self, s: str) -> bool:
        minL,maxL = 0,0
        for i in s:
            if i == "*":
                minL = max(minL-1,0)
                maxL +=1
            elif i == "(":
                minL,maxL = minL+1,maxL+1
            else:
                minL,maxL = minL-1,maxL-1
            if maxL<0:
                return False
        return 0 in range(minL,maxL+1)

        
class Solution:
    def checkValidString(self, s: str) -> bool:
        minB,maxB = 0,0
        for i in s:

            if i == "(":
                minB,maxB  = minB+1,maxB+1
            elif i == ")":
                minB,maxB  = minB-1,maxB-1
            else:
                minB,maxB = minB-1,maxB+1
            minB = max(0,minB)
            if maxB<0:
                return False
        print(minB,maxB)
        return 0 in range(minB,maxB+1)


        
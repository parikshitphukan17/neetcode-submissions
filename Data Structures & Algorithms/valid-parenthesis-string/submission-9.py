class Solution:
    def checkValidString(self, s: str) -> bool:
        maxBrack = 0
        minBrack = 0

        for c in s:
            if c == '(':
                maxBrack +=1
                minBrack +=1
            elif c == ')':
                maxBrack -=1
                minBrack -=1
            else:
                maxBrack +=1
                minBrack -=1
            if maxBrack <0:
                return False
            minBrack = max(0,minBrack)
        return 0 in range(minBrack,maxBrack+1)



        
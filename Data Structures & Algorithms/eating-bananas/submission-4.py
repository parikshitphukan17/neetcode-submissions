import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(rate):
            k = h
            for p in piles:
                if k<=0:
                    return False
                k -= math.ceil(p/rate)
            return k>=0

        l,r=1, max(piles)
        res = r
        while l<=r:
            m = (l+r)//2
            if isValid(m):
                res = min(res,m)
                r=m-1
            else:
                l = m+1
        return res

                

                
                
                



        
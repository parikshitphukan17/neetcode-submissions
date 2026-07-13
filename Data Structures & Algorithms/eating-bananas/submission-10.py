import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(cur,limit):
            for p in piles:
                limit -= math.ceil(p/cur)
                if limit<0:
                    return False
            return limit>=0

        l,r = 1,max(piles)
        res = None
        while l<=r:
            mid = (l+r)//2
            if check(mid,h):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
        
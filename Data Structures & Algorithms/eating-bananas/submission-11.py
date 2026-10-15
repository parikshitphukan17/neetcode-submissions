class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkSpeed(piles,sp,h):
            for b in piles:
                if h<=0:
                    return False
                h-=math.ceil(b/sp)
            return h>=0
        l,r = 1,max(piles)
        res = r
        while l<=r:
            m = (l+r)//2
            if checkSpeed(piles,m,h):
                res = min(res,m)
                r = m-1
            else:
                l=m+1
        return res
        
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = float("inf")
        def check(k):
            nonlocal h
            cur = 0
            for p in piles:
                if cur>h:
                    return False
                cur += math.ceil(p/k)
            return cur<=h


        while l<=r:
            m = (l+r)//2
            if check(m):
                res = min(res,m)
                r =m -1
            else:
                l =m+1
        return res



        
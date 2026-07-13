class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # [minVal,maxVal] -> binary search try if too small go right. if enough 
        # or too big save res and go left and retry
        N = len(piles)
        def check(val,piles):
            i = 0
            t = 0
            while i<N:
                t += math.ceil(float(piles[i])/val)
                i+=1
            return t

        l,r = 1,max(piles)
        res = r
        while l<=r:
            m = (l+r)//2
            t = check(m,piles)
            if t<=h:
                r=m-1
                res = min(res,m)
            else:
                l = m+1
        return res
            
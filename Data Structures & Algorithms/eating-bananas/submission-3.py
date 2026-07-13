class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l,r = 1,res
        while l<=r:
            mid = (l+r)//2
            totalHr = 0
            for i in piles:
                totalHr += math.ceil(float(i)/mid)
            if totalHr <=h:
                res = min(res,mid)
                r = mid-1
            else:
                l = mid +1
        return res

                

        
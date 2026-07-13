class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkBanana(val):
            time = 0
            i = 0
            while time<=h and i<len(piles):
                time += math.ceil(piles[i]/val)
                i+=1
            return time<=h
        l,r = 1,max(piles)
        res = None
        while l<=r:
            m = (l+r)//2
            if checkBanana(m):
                res = m
                r =m-1
            else:
                l =m+1
        return res

                
        
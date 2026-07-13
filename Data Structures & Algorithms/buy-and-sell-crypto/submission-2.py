class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        p = 0
        prev = prices[0]
        for cur in prices[1:]:
            if cur<prev:
                prev = cur
                continue
            p = max(p, cur-prev)
        return p 


        
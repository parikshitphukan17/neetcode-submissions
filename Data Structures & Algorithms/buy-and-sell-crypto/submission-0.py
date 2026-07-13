class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,p = prices[0],0
        for i in range(1,len(prices),1):
            s = prices[i]
            p = max(p,s-b)
            b = min(b,prices[i])
        return p
        
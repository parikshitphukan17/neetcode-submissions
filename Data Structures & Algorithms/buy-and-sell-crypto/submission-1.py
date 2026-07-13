class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        while i<len(prices):
            j=i+1
            print(i,j)
            while j<len(prices) and prices[j]>=prices[i]:
                res = max(prices[j]-prices[i],res)

                j+=1
            i = j
        return res



        # 10,1,5,6,7,1
        # B,S
        #    B,S,S,S,S
        
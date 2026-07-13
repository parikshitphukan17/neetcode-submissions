class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg,pos = 1,1
        s = -11
        for i in nums:
            nneg = min(neg*i,pos*i)
            npos = max(neg*i,pos*i)
            s = max(s,neg*i,pos*i)
            neg = min(nneg,1)
            pos = max(npos,1)
        return s


        
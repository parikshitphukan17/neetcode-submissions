class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        res = -1001
        for n in nums:
            res = max(prev+n,res)
            prev = max(n,prev+n,0)
        return res
    #     [2,-3,4,-2,2,1,-1,4]
    # prev = 0    
    # s = max(cur,prev+cur,s) 2
    # prev = max(cur,prev+cur) 2


    # prev = 2   
    # s = max(cur,prev+cur,s) 2
    # prev = max(cur,prev+cur,0) 0

    # prev = 0 
    # s = max(cur,prev+cur,s) 4
    # prev = max(cur,prev+cur,0) 4

    # prev =4
    # s = max(cur,prev+cur,s) 4
    # prev = max(cur,prev+cur,0) 2

    # prev =2
    # s = max(cur,prev+cur,s) 4
    # prev = max(cur,prev+cur,0) 4

    # prev =4
    # s = max(cur,prev+cur,s) 5
    # prev = max(cur,prev+cur,0) 5

    # prev =5
    # s = max(cur,prev+cur,s) 4
    # prev = max(cur,prev+cur,0) 4

        
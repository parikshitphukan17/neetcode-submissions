class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l,r = 0,0
        while r<len(nums)-1:
            res+=1
            nextR = r
            for i in range(l,r+1):
                nextR = max(nextR,i+nums[i])
            l = r+1
            r = nextR
        return res


            


        # 2   4   1   1   1   1

        # [2] 1 

        # [4,1] 2 

        
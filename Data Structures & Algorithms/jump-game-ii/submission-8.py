class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        N = len(nums)
        res = 0
        while True:
            if r == N-1:
                return res
            res +=1
            nextR = r
            for i in range(l,r+1,1):
                nextR = max(i+nums[i],nextR)
            if nextR>=N-1:
                return res
            l = r+1
            r = nextR
        




        

        
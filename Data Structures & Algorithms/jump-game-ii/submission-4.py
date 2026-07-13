class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        res = 0
        while True:
            if r >= len(nums)-1:
                return res
            nextR = 0
            while l<=r:
                nextR = max(l+nums[l],nextR)
                l+=1
            res +=1
            l = r+1
            r=nextR

        



        
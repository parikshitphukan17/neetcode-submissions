class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        l,r = 0,0
        while True:
            if r>=len(nums)-1:
                return cnt
            maxR =r
            while l<=r:
                maxR = max(l+nums[l],maxR)
                l+=1
            cnt +=1
            r = maxR
        




        # while l<=r
        # [2,4,1,1,1,1]
        # [2]
        # [4,1]
        
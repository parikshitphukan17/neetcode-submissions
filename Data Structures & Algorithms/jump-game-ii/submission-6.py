class Solution:
    def jump(self, nums: List[int]) -> int:
        u = 0
        l = 0
        res = 0
        while u<len(nums)-1:
            next = u
            for i in range(l,u+1):
                next = max(next,nums[i]+i)
            l,u = u+1,next
            res +=1
        return res
            
            





        
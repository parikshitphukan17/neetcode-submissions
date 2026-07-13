class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r,N = 0,0,len(nums)
        res = 0
        while l<N:
            if r>=N-1:
                return res
            maxR = 0
            while l<=r:
                maxR = max(maxR,nums[l]+l)
                l+=1
            res+=1
            l,r=r+1,maxR
        


        

        
        
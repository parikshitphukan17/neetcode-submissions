class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        N =len(nums)
        res = []
        while i<N:
            l,r =i+1,N-1
            n = nums[i]
            while l<r:
                s = n+nums[l]+nums[r]
                if s == 0:
                    res.append([n,nums[l],nums[r]])
                    while l+1<N and nums[l] == nums[l+1]:
                        l +=1
                    l +=1
                    while r-1>=0 and nums[r-1] == nums[r]:
                        r -=1
                    r -=1
                    
                if s<0:
                    while l+1<N and nums[l] == nums[l+1]:
                        l +=1
                    l +=1
                elif s>0:
                    while r-1>=0 and nums[r-1] == nums[r]:
                        r -=1
                    r -=1
            while i+1<N and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return res




  
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        N = len(nums)
        i = 0
        while i<N:
            n = nums[i]
            l,r = i+1,N-1
            while l<r:
                s=n+nums[l]+nums[r]
                if s == 0:
                    res.append([n,nums[l],nums[r]])
                    while l+1<N and nums[l] ==nums[l+1]:
                        l+=1
                    while r-1>i and nums[r-1] == nums[r]:
                        r-=1
                        
                    l+=1
                    r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
            while i+1<N and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return res






        # f   l               r
        # -4  -1  -1  0   1   2
        #  #when going to next look for non equal
        #  #if eqal to 0 move both l and r
        #  #else normal




        #  -
        # -2  0   1   1   2




        
        
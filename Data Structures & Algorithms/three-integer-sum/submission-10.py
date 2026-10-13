class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        N = len(nums)
        res = []
        while i<N:
            l= i+1
            r = N-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l+1<N and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                    while r-1>=0 and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                elif s<0:
                    while l+1<N and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                else:
                    while r-1>=0 and nums[r]==nums[r-1]:
                        r-=1
                    r-=1

            while i+1<N and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return res


        
            


        
        
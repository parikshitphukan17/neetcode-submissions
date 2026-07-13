class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur = 0
        N = len(nums)
        res = []
        def getNextLeft(l):
            while l+1<N and nums[l] == nums[l+1]:
                l+=1
            return l+1

        def getNextRight(r):
            while r-1>=0 and nums[r-1] == nums[r]:
                r-=1
            return r-1

        while cur<N:
            l = cur+1
            r = N-1
            while l<r:
                s = nums[cur]+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([nums[cur],nums[l],nums[r]])
                    l,r = getNextLeft(l),getNextRight(r)
            cur = getNextLeft(cur)
        return res


        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        res = nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                return min(res,nums[l])
            m = (l+r)//2
            res = min(res,nums[m])
            if nums[l]<=nums[m]:
                l = m+1
            else:
                r = m-1
        return res




        # l    r  m
        # [5,6,1,2,3,4]
        # [3,4,5,6,1,2]
        # if l<=r:
        #     return l
        # if l<=m: -> sorted array:
        #     if r<l:
        #         go right
        #     else return l
        # else:
        #     save res go left





        
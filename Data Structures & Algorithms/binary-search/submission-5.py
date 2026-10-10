class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if target < nums[m]:
                r = m-1
            else:
                l = m+1
        return -1



        #  0          r       5
        #  l      m   l   m   r
        # -1  0   2   4   6   8
        
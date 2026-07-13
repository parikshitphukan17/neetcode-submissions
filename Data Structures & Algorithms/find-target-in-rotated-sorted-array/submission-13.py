class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[m]>=nums[l]:
                if target>nums[m] or target<nums[l]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target>=nums[l] or target<nums[m]:
                    r = m-1
                else:
                    l =m+1
        return -1


    #    l        m       r
    #    [5   1   2   3   4]

        # l       m           r
        # 3   4   5   6   1   2


        # l       m           r
        # 5   6   0   1   2   3



        # 3   5   6   0   1   2


        # l       m           r
        # 3   5   6   0   1   2

        # if m>l:
        #     if target>m or target<l:
        #         go right
        #     else:
        #         go left
        # else:
        #     if target >l:
        #         go left
        #     else:
        #         go right



        
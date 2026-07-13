class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        # l.   m.l m r
        # [3,4,5,6,1,2]
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[l]<=nums[m]:
                if target>nums[m] or target<nums[l] :
                    l = m+1
                else:
                    r = m-1
            else:
                if target>nums[m]:
                    if target<nums[l]:
                        l = m+1
                    else:
                        r = m-1
                        
                else:
                    r = m-1
        return -1



        #     else:
        #         if target>

        # l.   m.    r          
        # [6,1,2,3,4,5]


        # if l<=m:
        #     if t>m: -> go right
        #     elif t<m:
        #         if t<l -> go right
        #         else:
        #             go left

        
        # else:
        #     if t>m:
        #         if t >l:
        #             go left
        #         else:
        #             go right
        #     else:
        #         go left





        
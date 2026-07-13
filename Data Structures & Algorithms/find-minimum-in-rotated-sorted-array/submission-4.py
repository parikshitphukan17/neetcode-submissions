class Solution:
    def findMin(self, nums: List[int]) -> int:


        ans = 1001
        l,r = 0,len(nums)-1
        while l<=r:
            if nums[l]<=nums[r]:
                return min(ans,nums[l])
            m = (l+r)//2
            ans = min(ans,nums[m])
            if nums[m]>=nums[l]:
                l = m+1
            else:
                r =m-1
        return ans

                        
        # l           m.  l   r
        # 3   4   5   6   1   2
        # m   l
        # l   r   m           r
        # 6   1   2   3   4   5

        # if l<r:
        #     ans = min(ans,l)
        #     return ans
        # if l>r:
        #     ans = m
        #     if m>=l
        #         go right
        #     else:
        #         go left
        
        
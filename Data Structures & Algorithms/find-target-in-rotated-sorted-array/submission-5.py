class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l]<= nums[m]:
                if target<nums[l] or target>nums[m]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target>nums[r] or target<nums[m]:
                    r = m-1
                else:
                    l =m+1
        return -1



# [5,6,1,2,3,4]
#         [3,4,5,6,1,2]
#         if l<=m:
#             if target<l or target>m:
#                 go right
#             else
#             go left
#         else:
#             target>r or target<m:
#             go left
#             else go right


        
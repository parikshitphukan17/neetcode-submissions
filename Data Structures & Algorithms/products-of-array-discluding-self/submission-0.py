class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left,right = [1]*len(nums),[1]*len(nums)
        for i in range(1,len(left),1):
            left[i] = left[i-1]*nums[i-1]
        for i in range(len(right)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        for i in range(len(nums)):
            left[i] *= right[i]
        return left

        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp ={}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==N:
                return 0
            rec = dfs(i+1,j)
            if j == -1 or nums[i]>nums[j]:
                rec = max(rec,1+ dfs(i+1,i))
            dp[(i,j)] =  rec
            return dp[(i,j)]
        return dfs(0,-1)


        
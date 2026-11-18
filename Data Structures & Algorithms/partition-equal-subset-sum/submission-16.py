class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        vis = set()
        s = sum(nums)
        if s%2 == 1:
            return False
        half = s//2
        N = len(nums)
        vis = set()
        def dfs(cur,i):
            if cur == half:
                return True
            if i == N or (cur,i) in vis:
                return False
            vis.add((cur,i))
            return dfs(cur+nums[i],i+1) or dfs(cur,i+1)
        return dfs(0,0)
            



        
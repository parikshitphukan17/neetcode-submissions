class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(cur,i):
            if i == len(nums):
                self.res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(cur,i+1)
            cur.pop()
            dfs(cur,i+1)
        dfs([],0)
        return self.res
        
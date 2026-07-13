class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(cur,i):
            if i == len(nums):
                return
            s = sum(cur)
            if s == target:
                res.append(cur.copy())
                return
            if s>target:
                return
            cur.append(nums[i])
            dfs(cur,i)
            cur.pop()
            dfs(cur,i+1)
        dfs([],0)
        return res

        
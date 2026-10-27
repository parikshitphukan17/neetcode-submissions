class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        res = []
        def dfs(i,cur,s):
            nonlocal target
            if i ==N or s>target:
                return
            s += nums[i]
            cur.append(nums[i])
            if s==target:
                res.append(cur.copy())
            elif s<target:
                dfs(i,cur,s)
            s -= nums[i]
            cur.pop()
            dfs(i+1,cur,s)
        dfs(0,[],0)
        return res
        
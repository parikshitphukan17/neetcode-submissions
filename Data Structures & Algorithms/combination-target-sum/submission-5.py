class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(nums)
        def dfs(i,cur):
            if i == N or sum(cur)>= target:
                if sum(cur) == target:
                    res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i,cur)
            cur.pop()
            dfs(i+1,cur)
        dfs(0,[])
        return res
        
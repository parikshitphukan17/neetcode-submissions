class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(nums)
        def dfs(i,cur,sm):
            if i == N or sm>target:
                return
            if sm == target:
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i,cur,sm+nums[i])
            cur.pop()
            dfs(i+1,cur,sm)
        dfs(0,[],0)
        return res
        
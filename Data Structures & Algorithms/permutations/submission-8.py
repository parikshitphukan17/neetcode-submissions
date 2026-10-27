class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums,cur):
            if not nums:
                res.append(cur.copy())
                return
            N = len(nums)
            for i in range(N):
                cur.append(nums[i])
                dfs(nums[:i]+nums[i+1:],cur)
                cur.pop()
        dfs(nums,[])
        return res

        
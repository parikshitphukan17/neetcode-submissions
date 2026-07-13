class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(nums,cur):
            if not nums:
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                cur.append(nums[i])
                dfs(nums[:i]+nums[i+1:],cur)
                cur.pop()
        dfs(nums,[])
        return res
        
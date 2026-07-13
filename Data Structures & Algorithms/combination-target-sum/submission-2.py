class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def dfs(i,cur):
            if i == len(nums):
                if sum(cur) == target:
                    res.append(cur.copy())
                return
            if sum(cur)>target:
                return
            
            cur.append(nums[i])
            dfs(i,cur)
            cur.pop()
            dfs(i+1,cur)
        dfs(0,[])
        return res        
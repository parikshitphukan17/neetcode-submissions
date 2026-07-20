class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        res = []
        def dfs(i,cur,s):
            if s == target:
                res.append(cur.copy())
                return
            if i ==N or s>target:
                return
            cur.append(nums[i])
            s+= nums[i]
            dfs(i,cur,s)
            s-= nums[i]
            cur.pop()
            dfs(i+1,cur,s)
        dfs(0,[],0)
        return res
            


        
        
        
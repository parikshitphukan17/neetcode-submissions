class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur,res = [],[]
        def dfs(inp):
            if not inp:
                res.append(cur.copy())
                return
            for i in range(len(inp)):
                cur.append(inp[i])
                dfs(inp[:i]+inp[i+1:])
                cur.pop()
        dfs(nums)
        return res
            
        
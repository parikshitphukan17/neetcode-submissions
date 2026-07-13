class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,cur,s):
            nonlocal target
            if s == target:
                res.append(cur.copy())
                return
            if i==len(candidates) or s>target:
                return
            cur.append(candidates[i])
            dfs(i+1,cur,s+candidates[i])
            cur.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur,s)
        dfs(0,[],0)
        return res
            


        
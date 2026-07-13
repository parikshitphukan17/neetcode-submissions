class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        def dfs(i,cur):
            if i == len(candidates):
                if sum(cur) == target:
                    res.append(cur.copy())
                return
            if sum(cur)>target:
                return
            cur.append(candidates[i])
            dfs(i+1,cur)
            cur.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur)
        dfs(0,[])
        return res

        
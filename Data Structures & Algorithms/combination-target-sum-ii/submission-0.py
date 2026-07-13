class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        l = len(candidates)
        def dfs(i,cur,s):
            if s == target:
                self.res.append(cur.copy())
                return
            if s>target or i>=l:
                return
            cur.append(candidates[i])
            dfs(i+1,cur,s+candidates[i])
            cur.pop()
            while i+1<l and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,cur,s)
        dfs(0,[],0)
        return self.res

                
        
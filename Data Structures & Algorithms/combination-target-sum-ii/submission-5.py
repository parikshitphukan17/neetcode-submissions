class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N,res = len(candidates),[]
        def dfs(i,cur,sm):
            if sm == target:
                res.append(cur.copy())
                return
            if i== N or sm>target:
                return 
            
            cur.append(candidates[i])
            dfs(i+1,cur,sm+candidates[i])
            j = i+1
            while j<N and candidates[j] == candidates[i]:
                j+=1
            cur.pop()
            dfs(j,cur,sm)
        dfs(0,[],0)
        return res
                
        
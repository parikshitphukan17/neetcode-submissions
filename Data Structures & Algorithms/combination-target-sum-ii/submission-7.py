class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        N = len(candidates)
        def dfs(i,cur):
            
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if i>=N or sum(cur)>target:
                return
            cur.append(candidates[i])
            dfs(i+1,cur)
            cur.pop()
            j = i+1
            while j<N and candidates[j] == candidates[i]:
                j+=1
            dfs(j,cur)
        dfs(0,[])
        return res
            





        # 9   2   2   4   6   1   5


        # 1   2   2   4   5   6   9



        #     1
        # /       /
        # 1           []2
        #         /       /
        #        2,2    []2
        #        so when going i+1 look for distinct 

        
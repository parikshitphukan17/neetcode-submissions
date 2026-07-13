class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(res,l,cur):
            if not cur:
                self.ans.append(res.copy())
                return
            i =0
            while i<l:
                res.append(cur[i])
                nx = cur[:i]+cur[i+1:]
                dfs(res,len(nx),nx)
                res.pop()
                i+=1
        dfs([],len(nums),nums)
        return self.ans
                





       

         
        
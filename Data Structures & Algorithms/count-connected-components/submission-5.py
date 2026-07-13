 



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        vis = set()
        def dfs(i,parent):
            if i in vis:
                return
            vis.add(i)
            for nei in adj[i]:
                if nei == parent:
                    continue
                dfs(nei,i)
        res = 0
        for i in range(n):
            if i not in vis:
                dfs(i,-1)
                res+=1
        return res

        


        
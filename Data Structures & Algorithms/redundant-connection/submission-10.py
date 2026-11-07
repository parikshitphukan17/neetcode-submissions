class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        def findParent(n):
            parent = par[n]
            while parent != par[parent]:
                par[parent] = par[par[parent]]
                parent = par[parent]
            return parent
        
        def union(e1,e2):
            p1,p2 = findParent(e1),findParent(e2)
            if p1 == p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2] = p1
                rank[p1] +=rank[p2]
            else:
                par[p1] = p2
                rank[p2] +=rank[p1]
            return True
        
        for e1,e2 in edges:
            if not union(e1,e2):
                return [e1,e2]

        
        
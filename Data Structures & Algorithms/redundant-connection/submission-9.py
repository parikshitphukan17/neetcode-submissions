class DSU:
    def __init__(self,n):
        self.rank = [1]*(n+1)
        self.par = [i for i in range(n+1)]


    def findParent(self,e):
        p = self.par[e]
        while p!= self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self,e1,e2):
        p1, p2 = self.findParent(e1),self.findParent(e2)
        if p1 == p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] +=self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for e1,e2 in edges:
            if not dsu.union(e1,e2):
                return [e1,e2]
        
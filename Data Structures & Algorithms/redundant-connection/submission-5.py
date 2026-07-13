class DSU:

    def __init__(self,n):
        self.rank = [1]*(n+1)
        self.par = {i:i for i in range(1,n+1)}
    
    def getParent(self,edge):
        p = self.par[edge]
        while p!= self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self,e1,e2):
        p1,p2 = self.getParent(e1),self.getParent(e2)
        if p1 == p2:
            return False
        if self.rank[p2]<self.rank[p1]:
            self.par[p2] = p1
            self.rank[p1] +=self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True




class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu =DSU(len(edges))
        for n1,n2 in edges:
            if not dsu.union(n1,n2):
                return [n1,n2]
            


        
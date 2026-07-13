class Union:

    def __init__(self,n):
        self.par,self.rank = {},{}
        for i in range(1,n+1):
            self.par[i] = i
            self.rank[i] = 0
    
    def getPar(self,n):
        while self.par[n] != n:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self,n1,n2):
        p1,p2 = self.getPar(n1),self.getPar(n2)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2] = p1
        if self.rank[p2]>self.rank[p1]:
            self.par[p1] = p2
        else:
            self.rank[p1]+=1
            self.par[p2] = p1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        u = Union(len(edges))
        for e1,e2 in edges:
            if not u.union(e1,e2):
                return [e1,e2]
        
        
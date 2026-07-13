class Union:
    def __init__(self,n):
        self.parent = {i : i for i in range(n+1)}
        self.rank = [0]*(n+1)

    def getParent(self,n1):
        while self.parent[n1] != n1:
            self.parent[n1] = self.parent[self.parent[n1]]
            n1 = self.parent[n1]
        return n1
    
    def union(self,n1,n2):
        par1,par2 = self.getParent(n1),self.getParent(n2)
        if par1 == par2:
            return False
        if self.rank[par1]>self.rank[par2]:
            self.parent[par2] = self.parent[par1]
        elif self.rank[par2]>self.rank[par1]:
            self.parent[par1] = self.parent[par2]
        else:
            self.rank[par1] +=1
            self.parent[par2] = self.parent[par1]
        return True
    

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        u = Union(len(edges))
        for n1,n2 in edges:
            if not u.union(n1,n2):
                return [n1,n2]
    




        
class Union:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0] *n
    
    def getParent(self,n1):
        while self.par[n1] != n1:
            self.par[n1] = self.par[self.par[n1]]
            n1 = self.par[n1]
        return n1

    def union(self,n1,n2):
        p1,p2 = self.getParent(n1),self.getParent(n2)
        if p1 == p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2]>self.rank[p1]:
            self.par[p1] = p2
        else:
            self.rank[p1] +=1
            self.par[p2] = p1
        return True
    


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = Union(n)
        for e1,e2 in edges:
            if u.union(e1,e2):
                n-=1
        return n

        
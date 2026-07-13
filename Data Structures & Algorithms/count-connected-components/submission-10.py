class Union:
    def __init__(self,n):
        self.rank = [0]*n
        self.par = {i:i for i in range(n)}
    

    def findParent(self,node):
        while self.par[node] != node:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node
    
    def union(self,n1,n2):
        p1,p2 = self.findParent(n1),self.findParent(n2)
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
        res = n
        for e1,e2 in edges:
            if u.union(e1,e2):
                res -=1
        return res


        
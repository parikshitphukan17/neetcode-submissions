class Union:
    def __init__(self,n):
        self.parent = {i:i for i in range(1,n+1)}
        self.rank = {i:0 for i in range(1,n+1)}

    def getPar(self,node1):
        while node1 !=self.parent[node1]:
            self.parent[node1] = self.parent[self.parent[node1]]
            node1 = self.parent[node1]
        return node1
    
    def union(self,n1,n2):
        p1,p2 = self.getPar(n1),self.getPar(n2)
        if p1 == p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1]<self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] +=1
        return True





class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        u = Union(len(edges))
        for e1,e2 in edges:
            if not u.union(e1,e2):
                return [e1,e2]


        
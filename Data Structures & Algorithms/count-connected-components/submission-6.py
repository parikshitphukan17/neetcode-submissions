class Unionfind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*(n)

    def getParent(self,node):
        print(self.parent)
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self,node1,node2):
        p1,p2 = self.getParent(node1),self.getParent(node2)
        if p1 == p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.parent[p1] = self.parent[p2]
        elif self.rank[p1]<self.rank[p2]:
            self.parent[p2] = self.parent[p1]
        else:
            self.parent[p1] = self.parent[p2]
            self.rank[p1] +=1
        return True
    


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = Unionfind(n)
        res = n
        for i,v in edges:
            if u.union(i,v):
                res -=1
        return res
        
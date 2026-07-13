class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent,rank = {},{}
        for i in range(1,len(edges)+1,1):
            parent[i] = i
            rank[i] = 0
        
        def find(n):
            p = parent[n]
            while p!= parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2] = p1
            elif rank[p2]>rank[p1]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] +=1
            return True
        for e1,e2 in edges:
            if not union(e1,e2):
                return [e1,e2]
            


        
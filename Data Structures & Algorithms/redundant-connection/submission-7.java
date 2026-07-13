class DSU {
    int[] parent,rank;
    public DSU(int n){
        parent = new int[n+1];
        rank = new int[n+1];
        for(int i = 0;i<=n;i++){
            parent[i] = i;
            rank[i] = 1;
        }

    }

    public int findParent(int e){
        int p = parent[e];
        while(p!=parent[p]){
            parent[p] = parent[parent[p]];
            p = parent[p];
        }
        return p;
    }

    public boolean union(int e1, int e2){
        var p1 = findParent(e1);
        var p2 = findParent(e2);
        if(p1==p2)
            return false;
        if(rank[p1]>rank[p2]){
            parent[p2] = p1;
            rank[p1] += rank[p2];
        } else {
            parent[p1] = p2;
            rank[p2] += rank[p1];
        }
        return true;
        
    }
}


class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        DSU dsu = new DSU(edges.length);
        for(int[] edge:edges){
            int e1 = edge[0],e2 = edge[1];
            if (!dsu.union(e1,e2)){
                return edge;
            }
        }
        return null;
        
    }
}

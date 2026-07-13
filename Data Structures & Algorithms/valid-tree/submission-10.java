class Solution {
    Set<Integer> vis = new HashSet<>();
    Map<Integer,List<Integer>> adj = new HashMap<>();
    public boolean validTree(int n, int[][] edges) {
        for(int i = 0;i<n;i++){
            adj.put(i,new ArrayList<>());
        }
        for(int[] edge:edges){
            int e1 = edge[0], e2 = edge[1];
            adj.get(e1).add(e2);
            adj.get(e2).add(e1);
        }
        return dfs(0,-1) && vis.size() == n;



        

    }
    public boolean dfs(int edge, int parent){
        if(vis.contains(edge)){
            return false;
        }
        vis.add(edge);
        for(int nei:adj.get(edge)){
            if(nei == parent)
                continue;
            if(!dfs(nei,edge))
                return false;
        }
        return true;
    }
}

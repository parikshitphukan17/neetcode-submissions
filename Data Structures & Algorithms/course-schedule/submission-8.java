class Solution {
    Map<Integer,List<Integer>> adj = new HashMap<>();
    Map<Integer,Boolean> vis = new HashMap<>();
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for(int i = 0;i<numCourses;i++){
            adj.put(i,new ArrayList<>());
        }
        for(int[] pre:prerequisites){
            int crs=pre[0], p = pre[1];
            adj.get(crs).add(p);
        }
        for(int i= 0; i<numCourses;i++){
            if(!dfs(i))
                return false;
        }
        return true;
    }

    public boolean dfs(int crs) {
        if(vis.containsKey(crs)){
            return vis.get(crs);
        }
        vis.put(crs,false);
        for(int pre:adj.get(crs)){
            if(!dfs(pre))
                return false;
        }
        vis.put(crs,true);
        return true;
    }
}

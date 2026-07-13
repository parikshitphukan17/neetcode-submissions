class Solution {
    int[] res;
    Map<Integer,Boolean> vis = new HashMap<>();
    Map<Integer,List<Integer>> map = new HashMap<>();
    int index = 0;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        res = new int[numCourses];
        for(int i=0;i<numCourses;i++){
            map.put(i,new ArrayList<>());
        }
        for(int[] crsPre: prerequisites){
            int crs = crsPre[0], pre = crsPre[1];
            map.get(crs).add(pre);
        }
        for(int i = 0;i<numCourses;i++){
            if(!dfs(i))
                return new int[]{};
        }
        return res;
        
    }

    public boolean dfs(int crs){
        if(vis.containsKey(crs)){
            return vis.get(crs);
        }
        vis.put(crs,false);
        for(int pre:map.get(crs)){
            if(!dfs(pre)){
                return false;
            }
        }
        vis.put(crs,true);
        res[index++] = crs;
        return true;
    }
}

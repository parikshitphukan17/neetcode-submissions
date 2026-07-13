class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {

        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            (a,b) -> Integer.compare(a[1],b[1])
        );

        Map<Integer,List<int[]>> adj = new HashMap<>();
        for(int i=1;i<=n;i++){
            adj.put(i,new ArrayList<>());
        }
        for(int[] time:times){
            int src= time[0],dest=time[1],cost=time[2];
            adj.get(src).add(new int[]{dest,cost});
        }
        int res = 0;
        minHeap.offer(new int[]{k,0});
        Set<Integer> vis = new HashSet<>();
        while(!minHeap.isEmpty() && vis.size()<n){
            int[] time = minHeap.poll();
            int src= time[0],cost = time[1];
            if(vis.contains(src))
                continue;
            res = cost;
            vis.add(src);
            for(int[] nextTime:adj.get(src)){
                int dest = nextTime[0], destTime = nextTime[1];
                minHeap.offer(new int[]{dest,cost+destTime});
            }
        }
        return vis.size()==n?res:-1;


        
    }
}

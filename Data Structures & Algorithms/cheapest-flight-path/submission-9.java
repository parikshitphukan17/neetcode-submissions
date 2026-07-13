class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        k++;
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            (a,b) -> Integer.compare(a[0],b[0])
        );
        minHeap.offer(new int[]{0,src});
        int res = 1001;
        Set<Integer> vis = new HashSet<>();
        Map<Integer,List<int[]>> adj = new HashMap<>();
        for(int[] flight:flights){
            int s = flight[0], d = flight[1], c = flight[2];
            adj.putIfAbsent(s,new ArrayList<>());
            adj.get(s).add(new int[] {c,d});
        }
        while(!minHeap.isEmpty() && k>=0){
            PriorityQueue<int[]> nextHeap = new PriorityQueue<>(
            (a,b) -> Integer.compare(a[0],b[0])
            );
            while(!minHeap.isEmpty()){
                int[] flight = minHeap.poll(); 
                int c = flight[0], s = flight[1];
                if(vis.contains(s)) {
                    continue;
                }
                if(s==dst){
                    res = Math.min(res,c);
                }
                if(!adj.containsKey(s)){
                    continue;
                }
                for(int[] nextFlight: adj.get(s)){
                    nextHeap.offer(new int[] {nextFlight[0]+c,nextFlight[1]});
                }
            }
            k--;
            minHeap = nextHeap;
        }
        return res<1001?res:-1;

    }
}

class Solution {
    public int leastInterval(char[] tasks, int n) {
        Deque<int[]> q = new LinkedList<>();
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a,b) -> Integer.compare(b[0],a[0]));
        Map<Integer,Integer> cnt = new HashMap<>();
        for(char t : tasks) {
            cnt.put(t-'a',cnt.getOrDefault(t-'a',0)+1);
            
        }
        for(Map.Entry<Integer,Integer> pair:cnt.entrySet()){
            maxHeap.offer(new int []{pair.getValue(),pair.getKey()});
        }
        int t = 0;
        while(q.size()>0 || maxHeap.size()>0) {
            t++;
            if(maxHeap.size()==0){
                t = Math.max(t,q.peek()[0]);
            }
            if(q.size()>0 && t==q.peek()[0]){
                var newTask = q.removeFirst();
                maxHeap.offer(new int []{newTask[2],newTask[1]});
            }
            var currentTask = maxHeap.poll();
            if(currentTask[0]-1>0){
                q.addLast(new int []{t+n+1,currentTask[1],currentTask[0]-1});
            }

        }
        return t;
        

        // t = 0
        // t++;
        // t = 1
        //         maxHeap    3A,2B,1C      q []
        //         maxHeap 2B,1C.  q [[5,ith,2]] 
        // t++;
        // t = 2
        //         maxHeap 2B,1C.  q [[5,A,2]] 
        //         maxHeap 1C.  q [[6,B,1],[5,A,2]]
        // t++;
        // t = 3   
        //         maxHeap 1C.  q[[6,B,1],[5,A,2]] 
        //         maxHeap   q[[6,B,1],[5,A,2]]  only add if greater than 0 tasks

        // t++;
        // t=4;
        // if no tasks remain take 1st from q and make t = max(t,1st time at q)
        // remove from q first if t == first from time in q
        // t = 5
        //         maxHeap 2A      q[[6,B,1]]
        //         maxHeap         q[[6,B,1], [9,A,1]]

                


        
    }
}

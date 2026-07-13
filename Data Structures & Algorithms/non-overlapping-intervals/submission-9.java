class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {

        Arrays.sort(intervals,Comparator.comparingInt((int[] a)->a[0])
            .thenComparingInt(a -> a[1]));
        int res = 0, last= -50001;
        for(int[] interval:intervals){
            if(last>interval[0]){
                res++;
                last = Math.min(last,interval[1]);
            } else {
                last = interval[1];
            }
        }
        return res;



        
    }
}

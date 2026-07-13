class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {

        List<int[]> res = new ArrayList<>();
        for(int i= 0;i<intervals.length;i++){
            int[] interval = intervals[i];
            int startNew= newInterval[0], endNew = newInterval[1], endPrev = interval[1],
            startPrev = interval[0];
            if(startNew>endPrev){
                res.add(interval);
            }  else if(endNew<startPrev) {
                res.add(newInterval);
                for(int j=i;j<intervals.length;j++){
                    res.add(intervals[j]);
                }
                return res.toArray(new int[0][]);

            } else if(startNew<=endPrev){
                newInterval = new int[]{Math.min(startPrev,startNew),Math.max(endNew,endPrev)};
            }
        }
        res.add(newInterval);
        return res.toArray(new int[0][]);

        
    }

    // if startNew>endPrev
    //     insert prev
    // elif startNew<=endPrev{
    //     update newInterval
    // } else if endNew<startPrev {
    //     insert new then merge rest of list and return

    // } 

}

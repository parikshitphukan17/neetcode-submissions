/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        
        intervals.sort((a,b) ->a.start-b.start);
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        int res = 0;
        for(Interval interval:intervals){
            minHeap.offer(interval.end);
            while(!minHeap.isEmpty() && minHeap.peek()<=interval.start){
                minHeap.poll();
            }
            res = Math.max(res,minHeap.size());
        }
        return res;

    }
}

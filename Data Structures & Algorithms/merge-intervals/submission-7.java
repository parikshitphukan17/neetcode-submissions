class Solution {
    public int[][] merge(int[][] intervals) {
        Deque<int[]> stack = new LinkedList<>();
        Arrays.sort(intervals,Comparator.comparingInt((int[] a)->a[0]).
            thenComparingInt(a->a[1]));
        for(int[] interval:intervals){
            int newStart = interval[0], newEnd = interval[1];
            if(stack.isEmpty()){
                stack.addLast(new int[]{newStart,newEnd});
                continue;
            }
            int prevEnd = stack.peekLast()[1];
            if(prevEnd>=newStart){
                int[] prev = stack.removeLast();
                stack.addLast(new int[]{Math.min(newStart,prev[0]), Math.max(newEnd,prev[1])});
            } else {
                stack.addLast(interval);
            }
        }
        return stack.stream().toArray(int[][]::new);
    }
}

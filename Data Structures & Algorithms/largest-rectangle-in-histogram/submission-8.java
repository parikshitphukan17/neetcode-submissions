class Solution {
    public int largestRectangleArea(int[] heights) {

        Deque<int[]> stack = new LinkedList<>();
        int area = 0;
        for(int i = 0;i<heights.length;i++){
            int h = heights[i];
            int l = i;
            System.out.println("h "+ h);
            while(!stack.isEmpty() && h<=stack.peekLast()[0]){
                int[] height = stack.removeLast();
                l = height[1];
                if(height[0]!=h){
                    area = Math.max(area,(i-l)*height[0]);
                }
            }
            stack.addLast(new int[]{h,l});
        }
        int r = heights.length;
        while(!stack.isEmpty()){
            int[] height = stack.removeLast();
            int l= height[1];
            int h = height[0];
            area = Math.max(area,(r-l)*h);
        }
        return area;


        // 7       7

        //                     4
        //             2   2
        //     1

        // enter into stack if empty
        // if not pop

        // 7,0
        // 7, 1,1     pop till last in stack is <= and take their start while cal their area
        // area = 7*r-l = 7
        // 1,0 7,2 2,3
        
        // 1,0 2,2 
        // area = 7*3-2 = 7

        // 1,0 2,2 2,3
        // 1,0 2,2
        // dont calc area if equal to prev

        // 1,0 2,2 4,5


        // area = 4
        // area = 2*4
        // area = 1* 6
        
    }
}

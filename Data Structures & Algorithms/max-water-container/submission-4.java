class Solution {
    public int maxArea(int[] heights) {
        int l,r;
        l = 0;
        r = heights.length-1;
        int area = 0;
        while(l<r){
            int a = (r-l) * Math.min(heights[l],heights[r]);
            area = Math.max(area,a);
            if(heights[l]<heights[r]){
                l++;
            } else{
                r--;
            }

        }
        return area;
        
    }
}

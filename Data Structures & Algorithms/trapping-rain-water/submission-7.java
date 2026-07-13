class Solution {
    public int trap(int[] height) {
        int l,r,leftMax,rightMax;
        l=0;
        r = height.length-1;
        leftMax = height[l];
        rightMax = height[r];
        int res = 0;
        while(l<r){
            if(leftMax<rightMax){
                l+=1;
                leftMax = Math.max(leftMax,height[l]);
                res += leftMax - height[l];

            } else{
                r-=1;
                rightMax = Math.max(rightMax,height[r]);
                res += rightMax-height[r];
            }
        }
        return res;
        // [0  2   0   3   1   0   1   3   2   1]


        //                                     0



    }
}

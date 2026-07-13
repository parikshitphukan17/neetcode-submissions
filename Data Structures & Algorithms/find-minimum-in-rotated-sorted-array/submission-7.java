class Solution {
    public int findMin(int[] nums) {
        int l = 0,r = nums.length-1, minVal = 1001;
        while(true){
            int m = (l+r)/2;
            if(nums[l]<=nums[r]){
                return Math.min(minVal,nums[l]);
            }
            if(nums[l]<nums[m]){
                minVal = Math.min(minVal,nums[l]);
                l=m+1;
            } else{
                if(nums[m]>nums[r]){
                    l=m+1;
                }
                else{
                    minVal = Math.min(minVal,nums[m]);
                    r = m-1;
                }
            }
        }

        // l       m   l   m   r
        // 3   4   5   6   1   2
        // m
        // l   r   m           r        
        // 6   1   2   3   4   5


        // l       m           r        
        // 5   6   1   2   3   4   

        // if l<r:
        //     return min(minval,l)
        // if l<m:
        //     minVal = min(minVal,l)
        //     move right
        // else:
            
        
        // l               m   l       m        r
        // 4   5   6   7   8   9   10  1   2   3



        
    }
}

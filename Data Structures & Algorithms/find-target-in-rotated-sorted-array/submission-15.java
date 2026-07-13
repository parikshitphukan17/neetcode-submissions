class Solution {
    public int search(int[] nums, int target) {

        int l=0,r =nums.length-1;
        while(l<=r){
            int m= (l+r)/2;
            if(nums[m]==target){
                return m;
            }
            if(nums[l]<nums[r]){
                if(nums[m]<target){
                    l=m+1;
                } else{
                    r =m-1;
                }
                
            } else {
                if(target<nums[m]){
                    if(nums[l]<=nums[m]){
                        if(target<nums[l]){
                            l =m+1;
                        } else {
                            r = m-1;
                        }
                    } else {
                        r = m-1;
                    }
                } else {
                    if(nums[l]<nums[m]) {
                        l = m+1;
                    } else {
                        if(target>=nums[l]){
                            r = m-1;
                        } else {
                            l=m+1;
                        }
                    }
                }
            }
        }
    return -1;

    }   

        // l       m
        // 6   1   2   3   4   5

        // l       m
        // 5   6   1   2   3   4


        // l       m           r
        // 3   4   5   6   1   2
        // if l<r:
        //     normal 
        
        // else{
        //     if target<m:
        //         if l<m:
        //             if target<l:
        //                 move right
        //             else :
        //                 move left
        //         else:
        //             move left
        //     else:
        //         if l<m:
        //             move right:
        //         else:
        //             if target>l:
        //                 move left
        //             else:
        //                 move right


                
}


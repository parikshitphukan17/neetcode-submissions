class Solution {
    public int missingNumber(int[] nums) {
        int res = 0;

        for(int i = 1;i<=nums.length;i++){
            res ^= i;
        }
        for(int n:nums){
            res ^=n;
        }
        return res;



        
        
    }
}

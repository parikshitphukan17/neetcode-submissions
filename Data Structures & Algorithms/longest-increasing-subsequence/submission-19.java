class Solution {
    Integer[][] dp;
    public int lengthOfLIS(int[] nums) {
        dp = new Integer[nums.length][nums.length+1];
        return dfs(0,-1,nums);
    }

    public int dfs(int i,int prev,int[] nums){
        if(nums.length == i){
            return 0;
        }
        if(dp[i][prev+1]!=null){
            return dp[i][prev+1];
        }
        int LIS = dfs(i+1,prev,nums);
        if(prev==-1 || nums[prev]<nums[i]){
            LIS = Math.max(LIS,1+dfs(i+1,i,nums));
        }
        dp[i][prev+1] = LIS;
        return LIS;
    }
}

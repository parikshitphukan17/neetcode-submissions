class Solution {
    Integer[] dp;
    public int rob(int[] nums) {
        dp = new Integer[nums.length+2];
        dp[nums.length] = 0;
        dp[nums.length+1] = 0;
        for(int i = nums.length-1;i>=0;i--){
            dp[i] = Math.max(nums[i]+dp[i+2],dp[i+1]);
        }
        return dp[0];
    }

    public int dfs(int index,int[] nums){
        if(index>=nums.length){
            return 0;
        }
        if(dp[index]!=null)
            return dp[index];
        dp[index] = Math.max(nums[index]+dfs(index+2,nums),dfs(index+1,nums));
        return dp[index];

    }
}

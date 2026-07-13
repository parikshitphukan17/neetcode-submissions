class Solution {
    Integer[] dp;
    public int rob(int[] nums) {
        dp = new Integer[nums.length];
        return dfs(0,nums);
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

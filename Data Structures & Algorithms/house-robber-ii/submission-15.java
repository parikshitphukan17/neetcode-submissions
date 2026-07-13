Integer[] dp;
class Solution {
    public int rob(int[] nums) {
        if(nums.length<=2){
            return Arrays.stream(nums).max().getAsInt();
        }
        dp = new Integer[nums.length+1];
        var cost1 = dfs(0,Arrays.copyOfRange(nums,0,nums.length-1));
        dp = new Integer[nums.length+1];
        return Math.max(cost1,dfs(0,Arrays.copyOfRange(nums,1,nums.length)));
        
    }

    public int dfs(int i, int[] nums){
        if(i>=nums.length){
            return 0;
        }
        if(dp[i]!=null){
            return dp[i];
        }
        dp[i] = Math.max(nums[i]+dfs(i+2,nums),dfs(i+1,nums));
        return dp[i];
    }
}

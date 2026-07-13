class Solution {
    Integer[][] dp;
    int total;
    public int findTargetSumWays(int[] nums, int target) {
        total = Arrays.stream(nums).sum();
        dp = new Integer[nums.length][((total+1)*2)];
        return dfs(0,0,nums,target);

        
    }

    public int dfs(int i, int s,int[] nums,int target){
        if(i==nums.length){
            if(s==target){
                return 1;
            }
            return 0;
        }
        if(dp[i][s+total] != null){
            return dp[i][s+total];
        }
        dp[i][s+total] = dfs(i+1,s+nums[i],nums,target) + dfs(i+1,s-nums[i],nums,target);
        return dp[i][s+total];
    }
}

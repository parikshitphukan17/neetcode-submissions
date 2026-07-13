class Solution {
    boolean dp[][];
    int sum;
    public boolean canPartition(int[] nums) {
        sum = Arrays.stream(nums).sum();
        if(sum%2!=0){
            return false;
        }
        dp = new boolean[nums.length][sum];
        return dfs(0,0,nums);

        
    }

    public boolean dfs(int i,int s, int[] nums){
        if(s==sum/2){
            return true;
        }
        if(s>sum/2 || i == nums.length){
            return false;
        }
        System.out.println(i+" "+s+" "+sum);
        if(dp[i][s]){
            return dp[i][s];
        }
        dp[i][s] = dfs(i+1,s+nums[i],nums) || dfs(i+1,s,nums) ;
        return dp[i][s];
    }
}

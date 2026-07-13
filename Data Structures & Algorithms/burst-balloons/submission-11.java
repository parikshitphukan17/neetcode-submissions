Integer[][] dp;
class Solution {
    public int maxCoins(int[] nums) {

        int[] copy = new int[nums.length+2];
        dp = new Integer[copy.length][copy.length];
        copy[0] = copy[nums.length+1] = 1;
        int k= 1;
        for(int i =0;i<nums.length;i++){
            copy[k++]=nums[i];
        }
        return dfs(0,copy.length-1,copy);
        
    }
  
    public int dfs(int l,int r,int[] nums){
        if(r-l==1)
            return 0;
        if(dp[l][r]!=null){
            return dp[l][r];
        }
        dp[l][r] = 0;
        for(int i = l+1;i<r;i++){
            int sum = nums[l]*nums[i]*nums[r];
            dp[l][r] = Math.max(dp[l][r],sum+dfs(l,i,nums)+dfs(i,r,nums));
        }
        return dp[l][r];

    }

}

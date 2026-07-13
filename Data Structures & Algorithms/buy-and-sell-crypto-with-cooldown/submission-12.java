class Solution {
    Integer[][] dp;
    public int maxProfit(int[] prices) {
        dp = new Integer[prices.length][2];
        return dfs(0,1,prices);
    }

    public int dfs(int i,int buy,int[] prices){
        if(i>=prices.length){
            return 0;
        }
        if(dp[i][buy]!=null){
            return dp[i][buy];
        }
        if(buy==1){
            dp[i][buy] = Math.max(-prices[i]+dfs(i+1,0,prices),dfs(i+1,buy,prices));
        } else{
            dp[i][buy] = Math.max(prices[i]+ dfs(i+2,1,prices),dfs(i+1,buy,prices));
        }
        return dp[i][buy];
    }
}

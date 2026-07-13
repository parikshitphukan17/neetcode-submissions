class Solution {
    Integer[][] dp;
    Integer amt;
    public int change(int amount, int[] coins) {
        dp = new Integer[coins.length][amount];
        amt = amount;
        return dfs(0,0,coins);
    }

    public int dfs(int i, int s, int[] coins){
        if(i>=coins.length || s>amt){
            return 0;
        }
        if(amt==s){
            return 1;
        }
        if(dp[i][s] != null){
            return dp[i][s];
        }
        dp[i][s] = dfs(i,s+coins[i],coins) + dfs(i+1,s,coins);
        return dp[i][s];
    }
}

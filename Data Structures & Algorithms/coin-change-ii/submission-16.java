class Solution {
    int[][] dp;
    Integer amt;
    public int change(int amount, int[] coins) {
        dp = new int[coins.length+1][amount+1];
        for(int[] arr:dp){
            arr[amount] = 1;
        }
        for(int i=coins.length-1;i>=0;i--){
            for(int j= amount-1;j>=0;j--){
                dp[i][j] = (j+coins[i]<=amount?dp[i][j+coins[i]]:0) + dp[i+1][j];
            }
        }
        return dp[0][0];
    }

    // public int dfs(int i, int s, int[] coins){
    //     if(i>=coins.length || s>amt){
    //         return 0;
    //     }
    //     if(amt==s){
    //         return 1;
    //     }
    //     if(dp[i][s] != null){
    //         return dp[i][s];
    //     }
    //     dp[i][s] = dfs(i,s+coins[i],coins) + dfs(i+1,s,coins);
    //     return dp[i][s];
    // }
}

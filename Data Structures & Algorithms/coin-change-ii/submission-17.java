class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount+1];
        dp[amount] = 1;
        for(int i=coins.length-1;i>=0;i--){
            int[] row = new int[amount+1];
            row[amount] = 1;
            for(int j= amount-1;j>=0;j--){
                row[j] = (j+coins[i]<=amount?row[j+coins[i]]:0) + dp[j];
            }
            dp = row;
        }
        return dp[0];
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

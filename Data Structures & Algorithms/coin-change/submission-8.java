class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        for(int i = 0;i<dp.length;i++){
            dp[i] = amount+1;
        }
        dp[0] = 0;
        for(int i = 1;i<=amount;i++){
            for(int c:coins){
                if(c<=i){
                    dp[i] = Math.min(dp[i],1+dp[i-c]);
                }
            }  
        }
        return dp[amount]<amount+1?dp[amount]:-1;


        // 0 = 0
        // 1 = 1 + dp[1-1]
        // 2 = 1 + dp[2-1]
        
    }
}

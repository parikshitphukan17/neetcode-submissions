class Solution {
    Integer[][] dp;
    public int longestCommonSubsequence(String text1, String text2) {
        dp = new Integer[text1.length()][text2.length()];
        return dfs(0,0,text1,text2);
    }

    public int dfs(int i1,int i2, String text1,String text2){
        if(i1 == text1.length() || i2 == text2.length()){
            return 0;
        }
        if(dp[i1][i2] != null) {
            return dp[i1][i2];
        }
        if(text1.charAt(i1)!= text2.charAt(i2)){
            dp[i1][i2] = Math.max(dfs(i1+1,i2,text1,text2),dfs(i1,i2+1,text1,text2));
        } else {
            dp[i1][i2] = 1 + dfs(i1+1,i2+1,text1,text2);
        }
        return dp[i1][i2];
    }
}

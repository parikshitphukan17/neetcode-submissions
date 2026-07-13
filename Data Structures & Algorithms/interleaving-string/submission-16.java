class Solution {
    boolean[][] dp;
    public boolean isInterleave(String s1, String s2, String s3) {
        int M = s1.length(), N = s2.length();
        dp = new boolean[M+1][N+1];
        dp[M][N] = true;
        if(M+N != s3.length())
            return false;
        for(int i=M;i>=0;i--){
            for(int j=N;j>=0;j--){
                if(dp[i][j])
                    continue;
                int k = i+j;
                dp[i][j] = (i<M && s1.charAt(i)==s3.charAt(k)?dp[i+1][j]:false) || 
                    (j<N && s2.charAt(j)==s3.charAt(k)?dp[i][j+1]:false);
            }
        }
        return dp[0][0];
        

        
    }

    // public boolean dfs(int i,int j,String s1,String s2,String s3){
    //     if(i==s1.length() && j == s2.length()){
    //         return true;
    //     }
    //     int k = i+j;
    //     if(dp[i][j]!=null)
    //         return dp[i][j];
    //     if(i<s1.length() && s1.charAt(i)==s3.charAt(k) && dfs(i+1,j,s1,s2,s3)){
    //         dp[i][j] = true;
    //         return true;
    //     } 
    //     if(j<s2.length() && s2.charAt(j)==s3.charAt(k) && dfs(i,j+1,s1,s2,s3)){
    //         dp[i][j] = true;
    //         return true;
    //     }
    //     dp[i][j] = false;
    //     return false;
    // }
}

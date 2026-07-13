class Solution {
    
    public boolean isInterleave(String s1, String s2, String s3) {
        int M = s1.length(), N = s2.length();
        boolean[] dp = new boolean[N+1];
        if(M+N != s3.length())
            return false;
        
        for(int i=M;i>=0;i--){
            boolean[] row = new boolean[N+1];
            if(i==M)
                row[N] = true;
            for(int j=N;j>=0;j--){
                if(row[j])
                    continue;
                int k = i+j;
                row[j] = (i<M && s1.charAt(i)==s3.charAt(k)?dp[j]:false) || 
                    (j<N && s2.charAt(j)==s3.charAt(k)?row[j+1]:false);
            }
            dp = row;
        }
        return dp[0];
        

        
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

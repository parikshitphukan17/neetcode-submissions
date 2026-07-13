class Solution {

    boolean[][] dp;
    int M,N;
    public boolean isMatch(String s, String p) {
        M = s.length();
        N=p.length();
        dp = new boolean[M+1][N+1];
        dp[M][N] = true;
        for(int i = M;i>=0;i--){
            for(int j = N-1;j>=0;j--){
                boolean isMatch = (i<M && (s.charAt(i)==p.charAt(j) || p.charAt(j) == '.'));
                if(j+1<N && p.charAt(j+1)=='*'){
                    dp[i][j] = dp[i][j] || (isMatch && dp[i+1][j]) || dp[i][j+2];
                } else if(isMatch){
                    dp[i][j] = dp[i][j] || dp[i+1][j+1];
                } 
            }
        }
        return dp[0][0];
    }

    // public boolean dfs(int i,int j, String s,String p){
    //     if(j==N){
    //         return i==M;
    //     }
    //     if(dp[i][j]!=null){
    //         return dp[i][j];
    //     }
    //     boolean isMatch = (i<M && (s.charAt(i)==p.charAt(j) || p.charAt(j) == '.'));
    //     if(j+1<N && p.charAt(j+1)=='*'){
    //         dp[i][j] = (isMatch && dfs(i+1,j,s,p)) || (dfs(i,j+2,s,p));
    //     }else if(isMatch){
    //         dp[i][j] = dfs(i+1,j+1,s,p);
    //     } else{
    //         dp[i][j] = false;
    //     }
    //     return dp[i][j];
    // }


    //             i

    // x   y   z   M

    // j
    // .   *   z
        
        
}

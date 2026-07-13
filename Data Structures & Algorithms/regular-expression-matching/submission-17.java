class Solution {

    int M,N;
    public boolean isMatch(String s, String p) {
        boolean[] dp;

        M = s.length();
        N=p.length();
        dp = new boolean[N+1];
        for(int i = M;i>=0;i--){
            boolean[] row = new boolean[N+1];
            if(i==M){
                row[N] = true;
            }
            for(int j = N-1;j>=0;j--){
                boolean isMatch = (i<M && (s.charAt(i)==p.charAt(j) || p.charAt(j) == '.'));
                if(j+1<N && p.charAt(j+1)=='*'){
                    row[j] = row[j] || (isMatch && dp[j]) || row[j+2];
                } else if(isMatch){
                    row[j] = row[j] || dp[j+1];
                } 
            }
            dp = row;
        }
        return dp[0];
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

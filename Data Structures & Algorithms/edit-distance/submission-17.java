class Solution {
    int M,N;
    public int minDistance(String word1, String word2) {
        M = word1.length();
        N = word2.length();
        int[] dp = new int[N+1];
        for(int j = 0;j<N;j++){
            dp[j] = N-j;
        }

        for(int i=M-1;i>=0;i--){
            int[] row = new int[N+1];
            row[N] = M-i;
            for(int j=N-1;j>=0;j--){
                if(word1.charAt(i) == word2.charAt(j)){
                    row[j] += dp[j+1];
                } else{
                    row[j] += 1+Math.min(dp[j+1],Math.min(row[j+1],dp[j]));
                }
            }
            dp = row;

        }
        return dp[0];
    }

    // public int dfs(int i,int j,String word1,String word2){
    //     if(i==M){
    //         if(j==N){
    //             return 0;
    //         }
    //         return N-j;
    //     }
    //     if(j == N){
    //        return M-i;
    //     }
    //     if(dp[i][j]!=null){
    //         return dp[i][j];
    //     }
    //     if(word1.charAt(i) == word2.charAt(j)){
    //         dp[i][j] = dfs(i+1,j+1,word1,word2);
    //     } else {
    //         dp[i][j] = 1 + Math.min(dfs(i,j+1,word1,word2),(Math.min(dfs(i+1,j,word1,word2),dfs(i+1,j+1,word1,word2))));
    //     }
    //     return dp[i][j];
    // }


        // i   i   i   i   i   i       
        // m   o   n   k   a   y   s   M
        
        // j   j   j   j   j   j
        // m   o   n   e   y   N


        // i   i   i   i   i
        // m   o   n   k   M

        // j   j   j   j   j   j
        // m   o   n   e   y   s   N

        // if i==M:
        //     if j==N:
        //         return 0
        //     return N-j-1;
        
        // if j==N:
        //     if i == M:
        //         return 0
        //     return M-i-1

            

        // if i==j:
        //     dfs(i+1,j+1)
        // if i!=j:
        //     1+min(insert,delete,replace).  insert = i,j+1. delete = i+1,j. replace = (i+1,j+1)
        
}

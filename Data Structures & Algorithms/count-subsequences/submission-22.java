Integer[][] dp;
class Solution {
    public int numDistinct(String s, String t) {
        dp = new Integer[s.length()+1][t.length()+1];
        
        //s.lengh<t.length: no subsequence
        if(s.length()<t.length()){
            return 0;
        }
        return dfs(0,0,s,t);
    }

    public int dfs(int i, int j, String s,String t){
        if(j == t.length()){
            return 1;
        }
        if(i== s.length()){
            return 0;
        }
        if(dp[i][j] != null){
            return dp[i][j];
        }

        if(s.charAt(i) == t.charAt(j)){
            dp[i][j] = dfs(i+1,j,s,t) + dfs(i+1,j+1,s,t);
        }else{
            dp[i][j] = dfs(i+1,j,s,t);
        }
        return dp[i][j];
    }



        // i
        // c   a   a   a   t

        
        // j
        // c   a   t

        // i == j = dfs(i+1,j), dfs(i+1,j+1)
        // if i!=j
        // dfs(i+1,j)


        // if j == M:
        //     return 1
        // if i == N:
        //     return 0

        
}

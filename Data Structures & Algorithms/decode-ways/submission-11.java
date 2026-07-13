
class Solution {
    int res = 0;
    Integer[] dp;
    public int numDecodings(String s) {
        dp = new Integer[s.length()];
        return dfs(0,s);
        
        
    }

    public int dfs(int i,String s){
        if(i==s.length()){
            return 1;
        }
        if(s.charAt(i)=='0'){
            return 0;
        }
        if(dp[i]!=null){
            return dp[i];
        }
        int value =i+1<s.length()?Integer.parseInt(s.substring(i,i+2)):0;
        if(value>0 && value<=26){
            dp[i] = dfs(i+1,s)+dfs(i+2,s);
        } else {
            dp[i] = dfs(i+1,s);
        }
        return dp[i];
    }

}

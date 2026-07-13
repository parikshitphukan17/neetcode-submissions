class Solution {
    Integer[][] dp;
    int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}};
    int M,N;
    public int longestIncreasingPath(int[][] matrix) {
        M = matrix.length;
        N = matrix[0].length;
        dp = new Integer[M][N];
        int res = 0;
        for(int i =0;i<M;i++){
            for(int j = 0;j<N;j++){
                res = Math.max(res,getMax(i,j,matrix));
            }
        }
        return res;
        
    }

    public int getMax(int i,int j,int[][] matrix){
        int res = 1;
        if(dp[i][j]!=null){
            return dp[i][j];
        }
        int nei = 0;
        for(int[] d:dir){
            int x = d[0]+i;
            int y = d[1]+j;
            if(x<0 || x==M ||y<0 || y==N || matrix[x][y]<=matrix[i][j]){
                continue;
            }
            nei= Math.max(nei,getMax(x,y,matrix));
        }
        dp[i][j] = res+nei;
        return dp[i][j];
    }
}

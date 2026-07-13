class Solution {
    Integer[][] grid;
    int ROWS,COLS;
    public int uniquePaths(int m, int n) {
        grid = new Integer[m+1][n+1];
        for(Integer[] row:grid){
            Arrays.fill(row,0);
        }
        grid[m-1][n-1] = 1;
        for(int i = m-1;i>=0;i--){
            for(int j = n-1;j>=0;j--){
                grid[i][j] += grid[i+1][j]+grid[i][j+1];
            }
        }
        return grid[0][0];
    }

    public int dfs(int i,int j){
        if(i==ROWS-1 && j == COLS-1){
            return 1;
        }
        if(i<0 || i==ROWS || j<0 || j==COLS){
            return 0;
        }
        if(grid[i][j] != null){
            return grid[i][j];
        }
        grid[i][j] = dfs(i+1,j) + dfs(i,j+1);
        return grid[i][j];
    }
}

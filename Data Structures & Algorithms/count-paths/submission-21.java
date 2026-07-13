class Solution {
    int ROWS,COLS;
    public int uniquePaths(int m, int n) {
        int[] grid = new int[n+1];
        Arrays.fill(grid,0);
        for(int i = m-1;i>=0;i--){
            int[] row = new int[n+1];
            if(i==m-1)
                row[n-1] = 1;
            for(int j = n-1;j>=0;j--){
                row[j] += grid[j]+row[j+1];
            }
            grid = row;
        }
        return grid[0];
    }

    // public int dfs(int i,int j){
    //     if(i==ROWS-1 && j == COLS-1){
    //         return 1;
    //     }
    //     if(i<0 || i==ROWS || j<0 || j==COLS){
    //         return 0;
    //     }
    //     if(grid[i][j] != null){
    //         return grid[i][j];
    //     }
    //     grid[i][j] = dfs(i+1,j) + dfs(i,j+1);
    //     return grid[i][j];
    // }
}

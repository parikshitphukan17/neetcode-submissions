class Solution {
    int ROWS,COLS;
    public int maxAreaOfIsland(int[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;
        int res = 0;
        for(int i=0;i<ROWS;i++){
            for(int j=0;j<COLS;j++){
                res = Math.max(res,dfs(i,j,grid));
            }
        }
        return res;

        
    }

    public int dfs(int i,int j, int[][] grid) {
        if(i<0 || j<0 || i == ROWS || j == COLS || grid[i][j] != 1){
            return 0;
        }
        int res = 1;
        grid[i][j] = 0;
        res += dfs(i+1,j,grid);
        res += dfs(i-1,j,grid);
        res += dfs(i,j+1,grid);
        res += dfs(i,j-1,grid);
        return res;
    }
}

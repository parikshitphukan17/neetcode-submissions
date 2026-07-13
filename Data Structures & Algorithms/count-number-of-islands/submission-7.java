class Solution {
    int ROWS,COLS;
    public int numIslands(char[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;
        int res = 0;
        for(int i=0;i<ROWS;i++){
            for(int j=0;j<COLS;j++){
                if(grid[i][j]=='1'){
                    res++;
                    count(i,j,grid);
                }
            }
        }
        return res;
        
        
    }

    public void count(int i,int j, char[][] grid){
        if(i<0 || j<0 || i==ROWS || j == COLS || grid[i][j] != '1'){
            return;
        }
        grid[i][j] = '0';
        count(i+1,j,grid);
        count(i,j+1,grid);
        count(i,j-1,grid);
        count(i-1,j,grid);

    }
}

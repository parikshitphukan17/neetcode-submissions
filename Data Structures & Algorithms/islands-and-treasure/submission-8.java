class Solution {
    boolean[][] vis;
    int ROWS,COLS,INF = 2147483647;
    public void islandsAndTreasure(int[][] grid) {
        Deque<int[]> q = new LinkedList<>();
        ROWS = grid.length;
        COLS = grid[0].length;
        int[][] directions = {{1, 0}, {-1, 0},
                                  {0, 1}, {0, -1}};
        vis = new boolean[ROWS][COLS];
        for(int i=0;i<ROWS;i++){
            for(int j=0;j<COLS;j++){
                if(grid[i][j]==0) {
                    q.addLast(new int[]{i,j});
                    vis[i][j] = true;
                }
            }
        }
        while(q.size()>0){
            var row = q.removeFirst();
            int r = row[0], c = row[1];
            int value = grid[r][c];
            for(int[] dir:directions){
                int nx = r+dir[0];
                int ny = c+dir[1];
                if(nx<0 || ny<0 || nx == ROWS || ny == COLS || vis[nx][ny] || grid[nx][ny]==-1){
                    continue;
                }
                vis[nx][ny] = true;
                grid[nx][ny] = Math.min(grid[nx][ny],value+1);
                q.addLast(new int[]{nx,ny});
            }
        }
        
    }
}

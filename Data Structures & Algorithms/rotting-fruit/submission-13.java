class Solution {
    public int orangesRotting(int[][] grid) {
        Deque<int[]> q = new LinkedList<>();
        int fresh = 0;
        int[][] directions = {{1, 0}, {-1, 0},
                                  {0, 1}, {0, -1}};
        int ROWS = grid.length, COLS = grid[0].length;
        boolean[][] vis = new boolean[ROWS][COLS];
        int t = 0;
        for(int i = 0;i<ROWS;i++){
            for(int j = 0;j<COLS;j++){
                if(grid[i][j] == 2){
                    q.addLast(new int[]{i,j});
                    vis[i][j] = true;

                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }
        if(fresh==0)
            return 0;
        while(!q.isEmpty() && fresh>0){
            Deque<int[]> nextQ = new LinkedList<>();
            t++;
            while(!q.isEmpty()){
                var row = q.removeFirst();
                int r = row[0], c = row[1];
                if(grid[r][c]==1){
                    fresh--;
                }
                for(int[] dir:directions){
                    int x = dir[0], y = dir[1];
                    int nx = x+r, ny = c+y;
                    if(nx<0 || ny<0 || nx==ROWS || ny == COLS || 
                        vis[nx][ny] || grid[nx][ny] != 1){
                        continue;
                    }
                    vis[nx][ny] = true;
                    nextQ.addLast(new int[] {nx,ny});
                }
            }
            q = nextQ;
        }
        return fresh==0? t-1:-1;

        
    }
}

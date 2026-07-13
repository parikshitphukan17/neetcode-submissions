class Solution {
    boolean[][] vis;
    int ROWS,COLS,res=0;
    PriorityQueue<int[]> minHeap = new PriorityQueue<>(
        (a,b)->Integer.compare(a[0],b[0])
    );
    int[][] directions = {{0,1},{1,0},{0,-1},{-1,0}};
    public int swimInWater(int[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;
        vis = new boolean[ROWS][COLS];
        minHeap.offer(new int[] {0,0,0});
        vis[0][0] = true;
        while(!minHeap.isEmpty()){
            int[] swim = minHeap.poll();
            int row = swim[1], col = swim[2];
            res = Math.max(res,grid[row][col]);
            if(row == ROWS-1 && col == COLS-1)
                return res;
            for(int[] dir: directions) {
                int neiRow = row +dir[0], neiCol = col+dir[1];
                if(neiRow<0 || neiRow== ROWS || neiCol<0 || 
                    neiCol == COLS || vis[neiRow][neiCol]) {
                    continue;
                }
                minHeap.offer(new int[] {grid[neiRow][neiCol],neiRow,neiCol});
                vis[neiRow][neiCol] = true;
            }
        }
        return -1;
    }
}

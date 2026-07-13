
class Solution {
    int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}};
    int ROWS,COLS;
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        ROWS = heights.length;
        COLS = heights[0].length;
        boolean[][] pac = new boolean[ROWS][COLS];
        boolean[][] atl = new boolean[ROWS][COLS];
        for(int j=0;j<COLS;j++){
            pac[0][j] = true; 
            atl[ROWS-1][j] = true;
        }

        for(int i=0;i<ROWS;i++) {
            pac[i][0] = true; 
            atl[i][COLS-1] = true;
        }
        bfs(heights, pac);
        bfs(heights, atl);
        for(int i=0;i<ROWS;i++){
            for(int j = 0;j<COLS;j++){
                if(pac[i][j] && atl[i][j]) {
                    List<Integer> ocean = new ArrayList<>();
                    ocean.add(i);
                    ocean.add(j);
                    res.add(ocean);
                }
                
            }
        }
        return res;
        

        
    }

    public void bfs(int[][] heights, boolean[][] ocean) {
        Deque<int[]> q = new LinkedList<>();
        boolean[][] vis = new boolean[ROWS][COLS];
        for(int i = 0;i<ROWS;i++){
            for(int j = 0;j<COLS;j++){
                if(ocean[i][j]) {
                    q.addLast(new int[]{i,j});
                    vis[i][j] = true;
                }
            }
        }
        
        while(!q.isEmpty()){
            int[] row = q.removeFirst();
            int r=row[0],c = row[1];
            ocean[r][c] = true;
            for(int[] d:dir){
                int dx = d[0], dy = d[1];
                int nx= r+dx,ny = c+dy;
                if(nx<0 || ny<0 || nx == ROWS || 
                    ny == COLS || heights[nx][ny]<heights[r][c] || vis[nx][ny]) {
                    continue;
                }
                vis[nx][ny] = true;
                q.addLast(new int[]{nx,ny});
            }

        }

    }
}

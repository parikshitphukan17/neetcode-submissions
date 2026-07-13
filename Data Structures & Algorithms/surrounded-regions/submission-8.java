class Solution {
    public void solve(char[][] board) {
        Deque<int[]> q = new LinkedList<>();
        int ROWS = board.length, COLS = board[0].length;
        int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}};
        for(int j = 0;j<COLS;j++){
            if(board[0][j] == 'O'){
                q.addLast(new int[]{0,j});
            }
            if(board[ROWS-1][j] == 'O'){
                q.addLast(new int[]{ROWS-1,j});
            }
        }

        for(int i = 1;i<ROWS-1;i++){
            if(board[i][0] == 'O'){
                q.addLast(new int[]{i,0});
            }
            if(board[i][COLS-1] == 'O'){
                q.addLast(new int[]{i,COLS-1});
            }
        }

        while(!q.isEmpty()){
            var row = q.removeFirst();
            int r = row[0], c= row[1];
            board[r][c] = 'T';
            for(int[] d:dir){
                int dx = d[0],dy = d[1];
                int nx=r+dx, ny = dy+c;
                if(nx<0 || ny<0 || nx == ROWS || ny == COLS || board[nx][ny]!= 'O'){
                    continue;
                }
                q.addLast(new int[]{nx, ny});
            }
        }

        for(int i = 0;i<ROWS;i++){
            for(int j = 0;j<COLS;j++){
                if(board[i][j] == 'T'){
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
            }
        }
        
    }
}

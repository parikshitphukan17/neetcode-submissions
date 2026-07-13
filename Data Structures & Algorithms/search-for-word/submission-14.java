class Solution {
    int ROWS,COLS;
    boolean[][]vis;
    public boolean exist(char[][] board, String word) {
        ROWS = board.length;
        COLS = board[0].length;
        vis = new boolean[ROWS][COLS];
        for(int i=0;i<ROWS;i++){
            for(int j=0;j<COLS;j++){
                if(dfs(i,j,0,word,board)){
                    return true;
                }
            }
        }
        return false;

    }

    public boolean dfs(int i, int j, int k, String word, char[][] board){
        if (k == word.length())
            return true;
        if(i<0 || j<0|| i==ROWS || j == COLS|| word.charAt(k) != board[i][j] || vis[i][j]){
            return false;
        }
        
        vis[i][j] = true;
        if (dfs(i+1,j,k+1,word,board) || dfs(i,j+1,k+1,word,board) || 
        dfs(i-1,j,k+1,word,board) || dfs(i,j-1,k+1,word,board))
            return true;
        vis[i][j] = false;
        return false;
    }
}

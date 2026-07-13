class Solution {
    Set<Integer> col = new HashSet<>();
    Set<Integer> posDiag = new HashSet<>();
    Set<Integer> negDiag = new HashSet<>();
    List<List<String>> res = new ArrayList<>();

    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for(char[] row: board){
            Arrays.fill(row,'.');
        }
        backtrack(0,n,board);
        return res;
    }
    public void backtrack(int r,int n, char[][] board){
        if(r == n){
            List<String> nqueen = new ArrayList<>();
            for(char[] row:board){
                nqueen.add(new String(row));
            }
            res.add(nqueen);
            return;
        }
        for(int c = 0;c<n;c++){
            if(col.contains(c) || posDiag.contains(c+r) || negDiag.contains(c-r)){
                continue;
            }
            col.add(c);
            posDiag.add(c+r);
            negDiag.add(c-r);
            board[r][c] = 'Q';
            backtrack(r+1,n,board);
            col.remove(c);
            posDiag.remove(c+r);
            negDiag.remove(c-r);
            board[r][c] = '.';

        }

    }
}

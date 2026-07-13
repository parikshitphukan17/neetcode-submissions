class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer,Set<Character>> col = new HashMap<>();
        Map<Integer,Set<Character>> row = new HashMap<>();

        int m = board.length;
        int n = board[0].length;
        for(int i = 0;i<m;i+=3){
            for(int j=0;j<n;j+=3){
                Set<Character> box = new HashSet<>();
                for(int r=i;r<i+3;r++){
                    row.putIfAbsent(r,new HashSet<>());
                    for(int c=j;c<j+3;c++){
                        col.putIfAbsent(c,new HashSet<>());
                        char val = board[r][c];
                        if(val == '.'){
                            continue;
                        }
                        if(row.get(r).contains(val) || col.get(c).contains(val) || box.contains(val)){
                            return false;
                        }
                        row.get(r).add(val);
                        col.get(c).add(val);
                        box.add(val);                    
                    }
                }

            }
        }
        return true;

        
    }
}

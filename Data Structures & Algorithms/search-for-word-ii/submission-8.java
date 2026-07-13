public class Node{
    Node[] children = new Node[26];
    boolean end = false;
}



class Solution {
    Node root = new Node();
    Set<String> result = new HashSet<>();
    boolean[][] visit;
    int rows,cols;
    public List<String> findWords(char[][] board, String[] words) {
        rows = board.length;
        cols = board[0].length;
        visit = new boolean[rows][cols];
        for(String w:words){
            var cur = root;
            for(char c:w.toCharArray()){
                var index = c-'a';
                if(cur.children[index]==null){
                    cur.children[index] = new Node();
                }
                cur = cur.children[index];
            }
            cur.end = true;
        }
        for(int i = 0;i<rows;i++){
            for(int j = 0;j<cols;j++){
                dfs(i,j,root,"",board);
            }
        }
        return new ArrayList<>(result);
        
    }

    public void dfs(int i, int j, Node node, String word, char[][] board){
        if(i<0 || j<0|| i==rows||j==cols||visit[i][j]||node.children[board[i][j]-'a'] == null){
            return;
        }
        visit[i][j] = true;
        node = node.children[board[i][j]-'a'];
        word += board[i][j];
        if(node.end){
            result.add(word);
        }
        dfs(i+1,j,node,word,board);
        dfs(i,j+1,node,word,board);
        dfs(i-1,j,node,word,board);
        dfs(i,j-1,node,word,board);
        visit[i][j] = false;
    }
}

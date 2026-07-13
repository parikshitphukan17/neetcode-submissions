class Node {
    Node[] children = new Node[26];
    boolean end = false;
}



class WordDictionary {
    Node root = new Node();
    public WordDictionary() {

    }

    public void addWord(String word) {
        var cur = root;
        for(char c:word.toCharArray()){
            if(cur.children[c-'a']==null){
                cur.children[c-'a']=new Node();
            }
            cur = cur.children[c-'a'];
        }
        cur.end = true;
    }

    public boolean search(String word) {
        return dfs(word,0,root);


    }
    public boolean dfs(String word,int j,Node node){
        var cur = node;
        for(int i = j;i<word.length();i++){
            var c = word.charAt(i);
            if(c == '.'){
                for(Node child: cur.children){
                    if(child!=null && dfs(word,i+1,child)){
                        return true;
                    }
                }
                return false;
            } else{
                if(cur.children[c-'a']==null){
                    return false;
                }
                cur = cur.children[c-'a'];
            }
        }
        return cur.end;
    }
}

class TreeNode {
    HashMap<Character,TreeNode> children = new HashMap<>();
    boolean end = false;
}



class PrefixTree {
    TreeNode root;
    public PrefixTree() {
        root = new TreeNode();
         
    }

    public void insert(String word) {
        var current = root;
        for(Character c:word.toCharArray()){
            if(!current.children.containsKey(c)){
                current.children.put(c,new TreeNode());
            }
            current = current.children.get(c);
        }
        current.end = true;

    }

    public TreeNode getNode(String word){
        var current = root;
        for(Character c:word.toCharArray()){
            if(!current.children.containsKey(c)){
                return null;
            }
            current = current.children.get(c);
        }
        return current;
    }

    public boolean search(String word) {
        var node = getNode(word);
        if(node == null){
            return false;
        }
        return node.end;

    }

    public boolean startsWith(String prefix) {
        return getNode(prefix)!=null;
        // if(node == null){
        //     return false;
        // }

    }
}

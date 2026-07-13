/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Codec {


    public String serialize(TreeNode root) {
        List<String> res = new LinkedList<>();
        dfs(root,res);
        return String.join(",",res);
    }

    public void dfs(TreeNode node,List<String> res){
        if(node==null){
            res.add("#");
            return;
        }
        res.add(String.valueOf(node.val));
        dfs(node.left,res);
        dfs(node.right,res);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Deque<String> q = new LinkedList<>();
        String[] array = data.split(",");
        Collections.addAll(q,array);
        return build(q);
    }

     //                 4
    //     2                    6
    // 1       3             5       7

    // [4,2,1,#,#,3,#,#,4,6,5,#,#,7,#,#]
    public TreeNode build(Deque<String> q){
        if(q.size() == 0)
            return null;
        var val = q.removeFirst();
        if(val.equals("#")){
            return null;
        }
        var root = new TreeNode(Integer.parseInt(val));
        root.left = build(q);
        root.right = build(q);
        return root;
    }
}

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

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        Deque<TreeNode> cur = new LinkedList<>();
        if(root == null){
            return res;
        }
        cur.addLast(root);
        while(cur.size()>0){
            Deque<TreeNode> child = new LinkedList<>();
            List<Integer> curRes = new ArrayList<>();
            while(cur.size()>0){
                var node = cur.removeFirst();
                curRes.add(node.val);
                if(node.left !=null){
                    child.addLast(node.left);
                }
                if (node.right!=null){
                    child.addLast(node.right);
                }
            }
            cur = child;
            res.add(curRes);
        }
        return res;

        
    }
}
